import jwt, datetime, pyotp, qrcode, io, base64
import sqlite3
from database import DB_PATH

SECRET_KEY = "your-access-secret"
REFRESH_SECRET = "your-refresh-secret"

def generate_mfa_secret():
    return pyotp.random_base32()

def get_mfa_uri(secret, username):
    return pyotp.totp.TOTP(secret).provisioning_uri(name=username, issuer_name="MyApp")

def generate_qr_base64(uri):
    img = qrcode.make(uri)
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def verify_otp(secret, otp):
    totp = pyotp.TOTP(secret)
    return totp.verify(otp)

def generate_access_token(user_id, role):
    payload = {
        'user_id': user_id,
        'role': role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
        'type': 'access'
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def generate_refresh_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'type': 'refresh'
    }
    return jwt.encode(payload, REFRESH_SECRET, algorithm='HS256')

# ---------- VERIFICATION FUNCTIONS (Add these) ----------
def verify_access_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        if payload.get('type') != 'access':
            return None
        return payload
    except:
        return None

def verify_refresh_token(token):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT token FROM token_blacklist WHERE token = ?", (token,))
    if c.fetchone():
        conn.close()
        return None
    conn.close()
    try:
        payload = jwt.decode(token, REFRESH_SECRET, algorithms=['HS256'])
        if payload.get('type') != 'refresh':
            return None
        return payload
    except:
        return None

def blacklist_refresh_token(token):
    try:
        payload = jwt.decode(token, REFRESH_SECRET, algorithms=['HS256'])
        expires = payload.get('exp')
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO token_blacklist (token, expires) VALUES (?, ?)", (token, expires))
        conn.commit()
        conn.close()
    except:
        pass
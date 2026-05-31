from flask import Flask, request, jsonify, render_template
from flask_bcrypt import Bcrypt
import database
import auth
import sqlite3

app = Flask(__name__)
bcrypt = Bcrypt(app)
database.init_db()

# ---------- API ROUTES (Backend) ----------

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'Server is running'})

@app.route('/')
def landing():
    return render_template('index.html')   # naya landing page

@app.route('/auth')
def auth_page():
    return render_template('auth.html')    # login/signup form


@app.route('/register', methods=['POST'])

def register():
    data = request.json
    username = data.get('username')
    password = bcrypt.generate_password_hash(data.get('password')).decode()
    role = data.get('role', 'user')
    mfa_secret = auth.generate_mfa_secret()
    conn = sqlite3.connect(database.DB_PATH)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password, role, mfa_secret) VALUES (?,?,?,?)",
                  (username, password, role, mfa_secret))
        conn.commit()
    except:
        return jsonify({'message': 'Username exists'}), 400
    conn.close()
    return jsonify({'message': 'User created', 'mfa_secret': mfa_secret})

@app.route('/mfa/qrcode', methods=['GET'])
def get_qr():
    username = request.args.get('username')
    conn = sqlite3.connect(database.DB_PATH)
    c = conn.cursor()
    c.execute("SELECT mfa_secret FROM users WHERE username = ?", (username,))
    row = c.fetchone()
    conn.close()
    if not row:
        return jsonify({'message': 'User not found'}), 404
    uri = auth.get_mfa_uri(row[0], username)
    qr_base64 = auth.generate_qr_base64(uri)
    return jsonify({'qr_base64': qr_base64})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    otp = data.get('otp')
    conn = sqlite3.connect(database.DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, password, role, mfa_secret FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    if not user or not bcrypt.check_password_hash(user[1], password):
        return jsonify({'message': 'Invalid credentials'}), 401
    if not auth.verify_otp(user[3], otp):
        return jsonify({'message': 'Invalid OTP'}), 401
    access_token = auth.generate_access_token(user[0], user[2])
    refresh_token = auth.generate_refresh_token(user[0])
    return jsonify({'access_token': access_token, 'refresh_token': refresh_token})

@app.route('/admin', methods=['GET'])
def admin_panel():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    payload = auth.verify_access_token(token)
    if not payload or payload.get('role') != 'admin':
        return jsonify({'message': 'Forbidden'}), 403
    return jsonify({'message': 'Welcome Admin'})

@app.route('/refresh', methods=['POST'])
def refresh():
    refresh_token = request.json.get('refresh_token')
    if not refresh_token:
        return jsonify({'message': 'Refresh token missing'}), 401
    payload = auth.verify_refresh_token(refresh_token)
    if not payload:
        return jsonify({'message': 'Invalid or expired refresh token'}), 401
    user_id = payload['user_id']
    conn = sqlite3.connect(database.DB_PATH)
    c = conn.cursor()
    c.execute("SELECT role FROM users WHERE id = ?", (user_id,))
    row = c.fetchone()
    conn.close()
    if not row:
        return jsonify({'message': 'User not found'}), 404
    new_access = auth.generate_access_token(user_id, row[0])
    return jsonify({'access_token': new_access})

@app.route('/logout', methods=['POST'])
def logout():
    refresh_token = request.json.get('refresh_token')
    if refresh_token:
        auth.blacklist_refresh_token(refresh_token)
    return jsonify({'message': 'Logged out successfully'})

# ---------- FRONTEND ROUTES (Interface) ----------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# ---------- RUN SERVER ----------
if __name__ == '__main__':
    app.run(debug=True)
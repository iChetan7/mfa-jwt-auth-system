import sqlite3
import os

# Vercel environment mein /tmp writable hota hai
if os.environ.get('VERCEL'):
    DB_PATH = '/tmp/app.db'
else:
    DB_PATH = 'instance/app.db'

def init_db():
    # Ensure directory exists (for local)
    db_dir = os.path.dirname(DB_PATH)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY,
                  username TEXT UNIQUE,
                  password TEXT,
                  role TEXT,
                  mfa_secret TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS token_blacklist
                 (token TEXT PRIMARY KEY, expires INTEGER)''')
    conn.commit()
    conn.close()

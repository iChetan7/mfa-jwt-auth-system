import sqlite3

DB_PATH = 'instance/app.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY,
                  username TEXT UNIQUE,
                  password TEXT,
                  role TEXT,
                  mfa_secret TEXT)''')
    # Blacklisted refresh tokens
    c.execute('''CREATE TABLE IF NOT EXISTS token_blacklist
                 (token TEXT PRIMARY KEY, expires INTEGER)''')
    conn.commit()
    conn.close()
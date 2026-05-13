# SECURE VERSION - All vulnerabilities from main branch have been fixed

import sqlite3
import subprocess
import hashlib
import os
import shlex

# ✅ FIX 1: SQL Injection → usar parametrized queries
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()

# ✅ FIX 2: Command Injection → evitar shell=True y sanitizar input
def ping_host(host):
    allowed_hosts = ["localhost", "127.0.0.1"]
    if host not in allowed_hosts:
        raise ValueError("Host not allowed")
    result = subprocess.run(
        ["ping", "-c", "1", host],
        shell=False,
        capture_output=True
    )
    return result.stdout

# ✅ FIX 3: Hash débil → usar bcrypt/sha256
def hash_password(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )
    return salt + key

# ✅ FIX 4: Deserialización insegura → usar json
import json
def load_session(data):
    return json.loads(data)

# ✅ FIX 5: Hardcoded secrets → usar variables de entorno
SECRET_KEY = os.environ.get("SECRET_KEY")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

def main():
    print("Secure app running...")
    print(get_user("admin"))
    print(hash_password("mypassword").hex())

if __name__ == "__main__":
    main()
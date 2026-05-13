# WARNING: Este código contiene vulnerabilidades intencionales para demostración

import sqlite3
import subprocess
import hashlib
import pickle
import os

# VULN 1: SQL Injection
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

# VULN 2: Command Injection
def ping_host(host):
    result = subprocess.run("ping -c 1 " + host, shell=True, capture_output=True)
    return result.stdout

# VULN 3: Hash debil (MD5)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# VULN 4: Deserializacion insegura
def load_session(data):
    return pickle.loads(data)

# VULN 5: Hardcoded secret
SECRET_KEY = "super-secret-password-123"
DB_PASSWORD = "admin1234"

def main():
    print("App running...")
    print(get_user("admin"))
    print(hash_password("mypassword"))

if __name__ == "__main__":
    main()
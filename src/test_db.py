# src/test_db.py
from db import get_connection

try:
    conn = get_connection()
    print("✅ Connected to the database!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)

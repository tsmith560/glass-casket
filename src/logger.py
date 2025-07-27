import os
import psycopg2
from dotenv import load_dotenv
from datetime import datetime

# Load env vars
load_dotenv()

# Database connection info
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def log_model_version(version_name, model_type, notes=None):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT id FROM model_versions WHERE version_name =%s", (version_name, ))
        result = cur.fetchone()
        if result:
            print(f"[INFO] Model version '{version_name}' already exists. ID: {result[0]}")
            return result[0]

        cur.execute("""
            INSERT INTO model_versions (version_name, model_type, date_registered, notes)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """, (version_name, model_type, datetime.now(), notes))
        version_id = cur.fetchone()[0]
        conn.commit()
        print(f"[INFO] Logged model version '{version_name}' with ID: {version_id}")
        return version_id
    
    finally:
        cur.close()
        conn.close()

def log_prediction(version_id, input_text, prediction_text):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO predictions (version_id, input_text, prediction_text, timestamp)
        VALUES (%s, %s, %s, %s);
    """, (version_id, input_text, prediction_text, datetime.now()))

    conn.commit()
    cur.close()
    conn.close()

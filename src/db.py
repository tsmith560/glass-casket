# src/db.py
import pg8000
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env into environment variables

def get_connection():
    return pg8000.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

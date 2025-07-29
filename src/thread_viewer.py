import streamlit as st
import json
from datetime import datetime
from src.config import MODEL_PROVIDER
from src.db import get_connection

# The oracle records the interaction in her journal
def log_interaction(question, response, model_version):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO interactions (timestamp, question, response, model_version) VALUES (NOW(), %s, %s, %s)",
        (question, response, model_version)
    )
    conn.commit()
    cursor.close()
    conn.close()

# Hear the echoes of the oracle
def view_thread():
    try:
        with open(LOG_PATH, "r") as f:
            log = json.load(f)
        for entry in log:
            print(f"\n🕰️  {entry['timestamp']}")
            print(f"⚰️  You: {entry['question']}")
            print(f"🔮 Oracle: {entry['response']}")
    except FileNotFoundError:
        print("No thread history found.")

# View thread log headstones
def view_thread_log():
    """Return a formatted string of thread history fetched from the DB for use in the UI."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT timestamp, question, response
            FROM interactions
            ORDER BY timestamp DESC
            LIMIT 100
        """)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        if not rows:
            return "🕸️ No thread history found."

        log_output = ""
        for entry in rows:
            timestamp, question, response = entry
            log_output += f"\n🕰️  {timestamp.isoformat()}\n"
            log_output += f"⚰️  You: {question}\n"
            log_output += f"🔮 Oracle: {response}\n"

        return log_output.strip()

    except Exception as e:
        return f"⚠️ Error retrieving thread history: {e}"

# View all log entries
def get_all_log_entries():
    """Return a list of all thread log entries (for use in the Necropolis UI)."""
    try:
        with open(LOG_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

from src.db import get_connection

# Get interactions for Thread Log display
def get_interactions(limit=100):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT timestamp, question, response, model_version
            FROM interactions
            ORDER BY timestamp DESC
            LIMIT %s
        """
        cursor.execute(query, (limit,))
        rows = cursor.fetchall()
        cursor.close()
        # return list of dicts for easy display
        return [
            {
                "timestamp": row[0].isoformat(),
                "question": row[1],
                "response": row[2],
                "model_version": row[3]
            }
            for row in rows
        ]
    except Exception as e:
        print(f"Error fetching interactions from DB: {e}")
        return []
    finally:
        if conn:
            conn.close()

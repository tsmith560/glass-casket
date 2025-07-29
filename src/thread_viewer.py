import streamlit as st
import json
from datetime import datetime
from config import MODEL_PROVIDER

LOG_PATH = "thread_log.json"

# The oracle records the interaction in her journal
def log_interaction(question, response, model_version):
    try:
        with open(LOG_PATH, "r") as f:
            log = json.load(f)
    except FileNotFoundError:
        log = []
    
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "response": response,
        "model_version": model_version
    }

    log.append(log_entry)

    with open(LOG_PATH, "w") as f:
        json.dump(log, f, indent=2)

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
    """Return a formatted string of thread history for use in the UI."""
    try:
        with open(LOG_PATH, "r") as f:
            log = json.load(f)
        
        log_output = ""
        for entry in log:
            log_output += f"\n🕰️  {entry['timestamp']}\n"
            log_output += f"⚰️  You: {entry['question']}\n"
            log_output += f"🔮 Oracle: {entry['response']}\n"
        
        return log_output.strip()
    
    except FileNotFoundError:
        return "🕸️ No thread history found."

# View all log entries
def get_all_log_entries():
    """Return a list of all thread log entries (for use in the Necropolis UI)."""
    try:
        with open(LOG_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
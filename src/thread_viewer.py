# src/thread_viewer.py

import json
from datetime import datetime

LOG_PATH = "thread_log.json"

def log_interaction(question, response):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "response": response,
    }
    try:
        with open(LOG_PATH, "r") as f:
            log = json.load(f)
    except FileNotFoundError:
        log = []

    log.append(entry)

    with open(LOG_PATH, "w") as f:
        json.dump(log, f, indent=2)

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

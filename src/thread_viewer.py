import json
from datetime import datetime
from config import MODEL_PROVIDER

LOG_PATH = "thread_log.json"

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

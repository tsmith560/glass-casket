# Boring stuff
import json
from datetime import datetime
from config import MODEL_PROVIDER
from mock_openai import MockOpenAIClient
from thread_viewer import log_interaction

# Update Oracle commit interactions to log file after answering
LOG_PATH = "thread_log.json"

def log_interaction(question, response):
    interaction = {
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "response": response
    }
    try:
        with open(LOG_PATH, "r") as f:
            log = json.load(f)
    except FileNotFoundError:
        log = []

    log.append(interaction)

    with open(LOG_PATH, "w") as f:
        json.dump(log, f, indent=2)

# Define Oracle class and call log_interaction
class Oracle:
    def __init__(self):
        if MODEL_PROVIDER == "openai":
            from openai import OpenAI
            self.client = OpenAI()
        elif MODEL_PROVIDER == "huggingface":
            from src.huggingface_client import HuggingFaceClient
            self.client = HuggingFaceClient()
        else:
            self.client = MockOpenAIClient()

# Define ask_oracle method
    def ask_oracle(self, question: str) -> str:
        messages = [{"role": "user", "content": question}]
        response = self.client.chat_completion(messages)
        content = response["choices"][0]["message"]["content"]
        log_interaction(question, content)
        return content

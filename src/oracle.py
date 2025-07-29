# Boring stuff
import json
from datetime import datetime
from config import MODEL_PROVIDER
from mock_openai import MockOpenAIClient
from thread_viewer import log_interaction

# Define Oracle class and call log_interaction
class Oracle:
    def __init__(self):
        if MODEL_PROVIDER == "openai":
            from openai import OpenAI
            self.client = OpenAI()
            self.model_version = "OpenAI GPT-4"
        elif MODEL_PROVIDER == "huggingface":
            from src.huggingface_client import HuggingFaceClient
            self.client = HuggingFaceClient()
            self.model_version = "HF - DistilBERT v1"
        else:
            self.client = MockOpenAIClient()
            self.model_version = "MockOpenAI v0.1"

# Define ask_oracle method
    def ask_oracle(self, question: str) -> str:
        messages = [{"role": "user", "content": question}]
        response = self.client.chat_completion(messages)
        content = response["choices"][0]["message"]["content"]
        log_interaction(question, content, model_version=self.model_version)
        return content

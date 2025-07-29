# src/oracle.py

from config import MODEL_PROVIDER
from mock_openai import MockOpenAIClient
# from src.huggingface_client import HuggingFaceClient (later)
# from src.openai_client import OpenAIClient (optional separate file)

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

    def ask_oracle(self, question: str) -> str:
        messages = [{"role": "user", "content": question}]
        response = self.client.chat_completion(messages)
        return response["choices"][0]["message"]["content"]


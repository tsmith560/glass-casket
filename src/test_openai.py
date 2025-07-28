# src/test_openai.py
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "What does the Exhumer do?"}]
)

print(response.choices[0].message["content"])

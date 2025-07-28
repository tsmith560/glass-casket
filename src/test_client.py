import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

USE_MOCK = True  # ← Toggle this to False later when you switch to Hugging Face or OpenAI

if USE_MOCK:
    from mock_openai import MockOpenAIClient as Client
    client = Client()
else:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Simulate calling the API
if USE_MOCK:
    response = client.chat_completion(messages=[
        {"role": "user", "content": "What does the Exhumer do?"}
    ])
    print(response["choices"][0]["message"]["content"])
else:
    response = client.chat.completions.create(
        model="gpt-4o",  # or any available model
        messages=[
            {"role": "user", "content": "What does the Exhumer do?"}
        ]
    )
    print(response.choices[0].message.content)

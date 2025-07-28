# src/runner.py

import openai
from dotenv import load_dotenv
import os
from logger import log_model_version, log_prediction

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_gpt4(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        print(f"[ERROR] Failed to get response from GPT-4: {e}")
        return None

if __name__ == "__main__":
    print("⚰️  Welcome to the Glass Casket Runner (a.k.a. Exhumer)")
    prompt = input("🧠 Enter your prompt: ")

    # STEP 1: Register (or reuse) model version
    version_name = "v1.1"  # For now, hardcoded; later this could be dynamic
    model_type = "GPT-4"
    notes = "Runner test via CLI"

    version_id = log_model_version(version_name, model_type, notes)
    print(f"[INFO] Using model version ID: {version_id}")

    # STEP 2: Call GPT-4
    output = call_gpt4(prompt)
    if output:
        print(f"\n💬 Model Response:\n{output}")

        # STEP 3: Log Prediction
        log_prediction(version_id, prompt, output)
        print(f"[INFO] Prediction logged.")
    else:
        print("⚠️ No output returned. Prediction not logged.")

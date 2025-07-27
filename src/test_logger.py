# src/test_logger.py
from logger import log_model_version, log_prediction

if __name__ == "__main__":

# Step 1: Log a model version
    version_id = log_model_version("v1.1", "GPT-4-vision", "Second test run")
    print(f"Logged model version with ID: {version_id}")

# Step 2: Log a prediction tied to that version
    log_prediction(version_id, "What is the future of AI?", "The AI sees a shimmering coffin sealed in glass.")
    print(f"Prediction logged.")
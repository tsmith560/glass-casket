import os

# Model selection: "mock", "openai", or "huggingface"
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "mock")

# API keys (safe to leave blank for mock)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")

# Helper toggles (derived from MODEL_PROVIDER)
USE_MOCK_CLIENT = MODEL_PROVIDER == "mock"
USE_OPENAI_CLIENT = MODEL_PROVIDER == "openai"
USE_HUGGINGFACE_CLIENT = MODEL_PROVIDER == "huggingface"

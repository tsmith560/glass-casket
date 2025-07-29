# Boring stuff
import json
from datetime import datetime
from src.config import MODEL_PROVIDER
from src.mock_openai import MockOpenAIClient
from src.thread_viewer import log_interaction

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

    # Import moon phase
    from src.utils import get_moon_phase_name

    # Define ask_oracle method
    def ask_oracle(self, question: str) -> str:
        response = self.client.chat_completion([{"role": "user", "content": question}])
        content = response["choices"][0]["message"]["content"]

        moon_phase = get_moon_phase_name()

        # Add custom responses per moon phase
        phase_responses = {
            "New Moon": "The void murmurs back in silence.",
            "Waxing Crescent": "A sliver of prophecy slices through the dark.",
            "First Quarter": "Doubt and clarity war for dominion.",
            "Waxing Gibbous": "Something stirs beneath the veil.",
            "Full Moon": "Revelation pierces like silver through shadow.",
            "Waning Gibbous": "Echoes of insight begin to fade.",
            "Last Quarter": "The Oracle dreams in fragments.",
            "Waning Crescent": "Only the dead are listening now."
        }

        gothic_whisper = phase_responses.get(moon_phase, "The moon hides its face...")

        final_response = f"{content}\n\n🌙 *[{moon_phase}]* {gothic_whisper}"

        log_interaction(question, final_response, model_version=self.model_version)
        return final_response


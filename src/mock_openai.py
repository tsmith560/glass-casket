class MockOpenAIClient:
    def __init__(self, *args, **kwargs):
        pass

    def chat_completion(self, messages):
        # Simulate a psychic response
        user_message = messages[-1]["content"]
        return {
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": f"🜃 The Exhumer is a vessel for memory. Its role is to retrieve lost data from beneath corrupted soil. You asked: '{user_message}'. I answer from the echo chamber of the void."
                    }
                }
            ]
        }

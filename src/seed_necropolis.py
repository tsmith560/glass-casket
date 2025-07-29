from necropolis import Necropolis

necro = Necropolis()

# Clear old data if you want to overwrite
necro.tombs = []

necro.add_tomb(
    model_version="MockOpenAI v0.1",
    description="Your first spectral guide, the warm-up dummy with cryptic answers.",
    date_introduced="2024-07-25",
    notable_traits=["mock responses", "cheap", "a bit eerie"],
    epitaph="Born of necessity, gone but not forgotten."
)

necro.add_tomb(
    model_version="OpenAI GPT-4o",
    description="The oracle that whispered forbidden knowledge with a flair.",
    date_introduced="2024-05-13",
    date_retired="2025-07-01",
    notable_traits=["multimodal", "fast", "friendly"],
    epitaph="It saw too much, too fast."
)

necro.add_tomb(
    model_version="HF-DistilBERT v1",
    description="Lightweight prophet from the Hugging Face realm.",
    date_introduced="2024-08-01",
    notable_traits=["fast", "efficient", "limited vision"],
    epitaph="Small but mighty."
)

print("🪦 Necropolis seeded with tombs:")
for tomb in necro.list_tombs():
    print(f"- {tomb['model_version']}: {tomb['epitaph']}")

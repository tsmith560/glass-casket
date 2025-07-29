# src/necropolis.py

import json
from datetime import datetime
from pathlib import Path

TOMBS_PATH = Path("model_tombs.json")

class Necropolis:
    def __init__(self, tombs_path=TOMBS_PATH):
        self.tombs_path = tombs_path
        self.tombs = self.load_tombs()

    def load_tombs(self):
        if not self.tombs_path.exists():
            # Start with an empty graveyard
            return []
        with open(self.tombs_path, "r") as f:
            return json.load(f)

    def save_tombs(self):
        with open(self.tombs_path, "w") as f:
            json.dump(self.tombs, f, indent=2)

    def add_tomb(self, model_version, description="", date_introduced=None,
                 date_retired=None, notable_traits=None, epitaph=""):
        if notable_traits is None:
            notable_traits = []

        # If no date introduced, default to today’s ISO date
        if date_introduced is None:
            date_introduced = datetime.now().date().isoformat()

        tomb = {
            "model_version": model_version,
            "description": description,
            "date_introduced": date_introduced,
            "date_retired": date_retired,
            "notable_traits": notable_traits,
            "epitaph": epitaph,
        }
        self.tombs.append(tomb)
        self.save_tombs()

    def list_tombs(self):
        return self.tombs

    def find_tomb(self, model_version):
        for tomb in self.tombs:
            if tomb["model_version"] == model_version:
                return tomb
        return None

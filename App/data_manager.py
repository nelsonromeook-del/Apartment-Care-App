# data_manager.py
# Compatible with the team's codebase

import json
import os


class DataManager:
    def __init__(self, file_path: str):
        """
        file_path example: "data/users.json"
        """
        self.file_path = file_path
        self._ensure_file()

    # -----------------------------
    # File setup
    # -----------------------------
    def _ensure_file(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)

    # -----------------------------
    # Instance methods
    # -----------------------------
    def load(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save(self, data):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    # -----------------------------
    # Static methods
    # -----------------------------
    @staticmethod
    def read_file(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    @staticmethod
    def write_file(file_path, data):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
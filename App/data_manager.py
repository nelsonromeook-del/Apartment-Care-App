# data_manager.py

import json
import os



class DataManager:
    def __init__(self, file_path: str):
        """
        file_path example: "Data/users.json"
        """
        self.file_path = file_path
        self._ensure_file()


    def _ensure_file(self):
    
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)

    def load(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save(self, data):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)


    @staticmethod
    def read_file(file_path):

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

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
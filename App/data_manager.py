# This file is used to create json fiiles to store data


import json
import os
import uuid
from typing import Any, List


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "Data")

class JSONRepository:

    def __init__(self, filename:str):
        self.path = os.path.join(DATA_DIR, filename)
        self._ensure_file()
        
    
    def _ensure_file(self):
        os.makedirs(DATA_DIR,exist_ok=True)
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as file:
                json.dump([], file, indent=4)

    def load(self) -> List[dict]:
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def save(self,data: List[dict]):
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)


    #------------CRUD--------------

    def get_all(self) -> List[dict]:
        return self.load()
    
    def find_by_id(self, item_id: str) -> dict:
        data = self.load()
        return next((item for item in data if item["id"] == item_id), None)
    
    def add(self, item: dict) -> dict:
        data = self.load()
        item["id"] = str(uuid.uuid4())
        data.append(item)
        self.save(data)
        return item
    
    def update(self, item_id: str, updates: dict) -> bool:
        data = self.load()
        for item in data:
            if item["id"] == item_id:
                item.update(updates)
                self.save(data)
                return True
        return False
    
    def delete(self, item_id: str) -> bool:
        data = self.load()
        new_data = [item for item in data if item["id"] != item_id]

        if len(new_data) == len(data):
            return False

        self.save(new_data)
        return True


class UserRepository(JSONRepository):
    def __init__(self):
        super().__init__("users.json")

    def find_by_email(self, email: str) -> dict:
        users = self.load()
        return next((u for u in users if u["email"] == email), None)



class IssueRepository(JSONRepository):
    def __init__(self):
        super().__init__("issues.json")


class AnnouncementRepository(JSONRepository):
    def __init__(self):
        super().__init__("announcements.json")

  
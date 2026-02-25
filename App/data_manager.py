# This file is used to create json fiiles to store data


import json
import os
from typing import Any, List


BASE_DIR = os.paht.dir(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "Data")

class JSONRepository:
    """
    Base repository class that handlles all JSON file I/O operations
    """

    def __init__(self, filename:str):
        self.filename = filename
        self.path = os.path(DATA_DIR, filename)
        self._ensure_file()
        
    
    def _ensure_file(self):
        os.makedirs(DATA_DIR,exist_ok=True)
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)

    def load(self) -> List[Any]:
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return[]
        
    def save(self,data: List[Any]) -> None:
        with open(self.path, "W", encoding="utf"-8) as file:
            json.dump(data, file, indent=4)



class UserRepository(JSONRepository):
    def __init__(self):
        super().__init__("users.json")


class IssueRepository(JSONRepository):
    def __init__(self):
        super().__init__("issues.json")


class AnnouncementRepository(JSONRepository):
    def __init__(self):
        super().__init__("announcements.json")


class RentRepository(JSONRepository):
    def __init__(self):
        super().__init__("rents.json")      
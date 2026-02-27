from data_manager import DataManager
import hashlib


class User:
    def __init__(self, house, role):
        self._house = house
        self._role = role

    @property
    def house(self):
        return self._house

    @property
    def role(self):
        return self._role


class AuthManager:
    def __init__(self):
        self.data_manager = DataManager("Data/users.json")


    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest() # Hashing the password using SHA-256 
    
    def user_exists(self, house):
        users = self.data_manager.load()
        return any(user.get("house") == house for user in users)

    
    def register_user(self, house, password, role):
        if self.user_exists(house):
            return False

        hashed_password = self.hash_password(password)

        users = self.data_manager.load()
        users.append({
            "house": house,
            "password": hashed_password,
            "role": role
        })
        self.data_manager.save(users)
        return True

    
    def login(self, house, password):
        users = self.data_manager.load()
        hashed_password = self.hash_password(password)

        for user in users:
            if user["house"] == house and user["password"] == hashed_password:
                return User(user["house"], user["role"])

        return None
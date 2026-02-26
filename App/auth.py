from data_manager import DataManager
import hashlib


class User:
    def __init__(self, username, role):
        self._username = username
        self._role = role

    @property
    def username(self):
        return self._username

    @property
    def role(self):
        return self._role


class AuthManager:
    def __init__(self):
        self.data_manager = DataManager("data/users.json")


    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest() # Hashing the password using SHA-256

    def user_exists(self, username):
        users = self.data_manager.load()
        return any(user["username"] == username for user in users)

    
    def register_user(self, username, password, role):
        if self.user_exists(username):
            return False

        hashed_password = self.hash_password(password)

        users = self.data_manager.load()
        users.append({
            "username": username,
            "password": hashed_password,
            "role": role
        })
        self.data_manager.save(users)
        return True

    
    def login(self, username, password):
        users = self.data_manager.load()
        hashed_password = self.hash_password(password)

        for user in users:
            if user["username"] == username and user["password"] == hashed_password:
                return User(user["username"], user["role"])

        return None
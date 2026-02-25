from data_manager import DataManager


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

    def user_exists(self, username):
        users = self.data_manager.load()
        return any(user["username"] == username for user in users)

    def register_user(self, username, role):
        if self.user_exists(username):
            return False

        users = self.data_manager.load()
        users.append({
            "username": username,
            "role": role
        })
        self.data_manager.save(users)
        return True

    def login(self, username):
        users = self.data_manager.load()
        for user in users:
            if user["username"] == username:
                return User(user["username"], user["role"])
        return None
# main.py – Application entry point

from auth import AuthManager
from menu import Menu


class ApartmentCareApp:
    def __init__(self):
        self.auth = AuthManager()

    def run(self):
        while True:
            print("-------------- ApartmentCare App ---------------")
            print("""
            1. Register
            2. Login
            3. Exit
            """)

            choice = input("Enter a choice: ").strip()

            # ---------------- REGISTER ----------------
            if choice == "1":
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                role = input("Role (tenant/admin): ").strip().lower()

                if role not in ("tenant", "admin"):
                    print("Invalid role ❌")
                    continue

                success = self.auth.register_user(username, password, role)

                if success:
                    print("Registered successfully 😎")
                else:
                    print("User already exists 💀")

            # ---------------- LOGIN ----------------
            elif choice == "2":
                username = input("Username: ").strip()
                password = input("Password: ").strip()

                user = self.auth.login(username, password)

                if not user:
                    print("Invalid login ❌")
                else:
                    # Convert User object → dict (Menu expects dict)
                    user_data = {
                        "username": user.username,
                        "role": user.role
                    }

                    Menu(user_data).run()

            # ---------------- EXIT ----------------
            elif choice == "3":
                print("Goodbye 👋")
                break

            else:
                print("Invalid choice, try again")


if __name__ == "__main__":
    ApartmentCareApp().run()
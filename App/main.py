# main.py – Application entry point

from auth import AuthManager
from menu import Menu
from colorama import init
from colorama import Fore, Style 

init(autoreset=True)


class ApartmentCareApp:
    def __init__(self):
        self.auth = AuthManager()

    def run(self):
        while True:
            print(Fore.CYAN + Style.BRIGHT + "-------------- ApartmentCare App ---------------")
            print(Fore.BLUE + Style.BRIGHT + """
            1. Register
            2. Login
            3. Exit
            """)

            choice = input("Enter a choice: ").strip()

            # ---------------- REGISTER ----------------
            if choice == "1":
                house = input("House Number: ").strip()
                password = input("Password: ").strip()
                role = input("Role (tenant/admin): ").strip().lower()

                if role not in ("tenant", "admin"):
                    print(Fore.RED + Style.BRIGHT + "Invalid role ❌")
                    continue

                success = self.auth.register_user(house, password, role)

                if success:
                    print(Fore.GREEN + "Registered successfully 😎")
                else:
                    print(Fore.RED + "User already exists 💀")

            # ---------------- LOGIN ----------------
            elif choice == "2":
                house = input("House Number: ").strip()
                password = input("Password: ").strip()

                user = self.auth.login(house, password)

                if not user:
                    print(Fore.RED + "Invalid login ❌")
                else:
                    # Convert User object → dict (Menu expects dict)
                    print(Fore.GREEN + Style.BRIGHT + "Login Successful😎")
                    user_data = {
                        "house": user._house,
                        "role": user.role
                    }
                    Menu(user_data).run()

            # ---------------- EXIT ----------------
            elif choice == "3":
                print(Fore.MAGENTA + Style.BRIGHT + "Goodbye 👋")
                break

            else:
                print(Fore.RED + Style.BRIGHT + "Invalid choice, try again")


if __name__ == "__main__":
    ApartmentCareApp().run()
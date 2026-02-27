#This is the dashboard for the users and admin depending on who has logged in
from issues import IssueManager
from announcements import AnnouncementManager
from colorama import Fore, Style


class Menu:# Menu class for a property management system
    def __init__(self, user):
        self.user = user
        self.issue_manager = IssueManager()
        self.announcement_manager = AnnouncementManager()

    def run(self):
        if self.user["role"] == "tenant":
            self.tenant_menu()
        elif self.user["role"] == "admin":
            self.admin_menu()
        else:
            print("Invalid role.")

    def tenant_menu(self):
        while True:
            print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "\n--- TENANT DASHBOARD ---")
            print(Fore.CYAN + "1. View Announcements")
            print("2. Report Issue")
            print(Fore.YELLOW + "3. View My Issues")
            print("4. Logout")

            choice = input("Choose: ")

            if choice == "1":
                self.announcement_manager.view_announcements()

            elif choice == "2":
                desc = input("Describe issue: ").strip()
                if desc:
                    self.issue_manager.add_issue(self.user["house"], desc)
                else:
                    print("Description cannot be empty.")

            elif choice == "3":
                issues = self.issue_manager.get_user_issues(self.user["house"])

                if not issues:
                    print(Fore.YELLOW + "No issues reported yet🧷")
                for issue in issues:
                    print(issue)

            elif choice == "4":
                break
            else:
                print(Fore.RED + Style.BRIGHT + "Invalid choice.")

    def admin_menu(self):
        while True:
            print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "\n--- ADMIN DASHBOARD ---")
            print(Fore.CYAN + "1. View All Issues")
            print("2. Update Issue Status")
            print(Fore.YELLOW + "3. Add Announcement")
            print("4. Logout")

            choice = input("Choose: ")

            if choice == "1":
                for issue in self.issue_manager.issues:
                    print(issue)

            elif choice == "2":
                print("Resolved or Pending")
                try:
                    issue_id = int(input("Issue ID: "))
                    status = input("New Status: ")
                    self.issue_manager.update_issue_status(issue_id, status)
                except ValueError:
                    print(Fore.RED + Style.BRIGHT + "Invalid ID.")

            elif choice == "3":
                msg = input("Announcement message: ").strip()
                if msg:
                    self.announcement_manager.add_announcement(
                        msg, self.user["house"]
                    )
                else:
                    print(Fore.YELLOW + Style.BRIGHT + "Message cannot be empty.")

            elif choice == "4":
                break
            else:
                print(Fore.RED + Style.BRIGHT + "Invalid choice.")
#This is the dashboard for the users and admin depending on who has logged in
from issues import IssueManager
from announcements import AnnouncementManager


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
            print("\n--- TENANT DASHBOARD ---")
            print("1. View Announcements")
            print("2. Report Issue")
            print("3. View My Issues")
            print("4. Logout")

            choice = input("Choose: ")

            if choice == "1":
                self.announcement_manager.view_announcements()

            elif choice == "2":
                desc = input("Describe issue: ").strip()
                if desc:
                    self.issue_manager.add_issue(self.user["username"], desc)
                else:
                    print("Description cannot be empty.")

            elif choice == "3":
                issues = self.issue_manager.get_issues_by_house(self.user["username"])
                for issue in issues:
                    print(issue)

            elif choice == "4":
                break
            else:
                print("Invalid choice.")

    def admin_menu(self):
        while True:#Displays a loop-based dashboard for admins with 4 options:
            print("\n--- ADMIN DASHBOARD ---")
            print("1. View All Issues")
            print("2. Update Issue Status")#Update Issue Status — admin enters an issue ID and a new status (e.g. "resolved"), with error handling for invalid input
            print("3. Add Announcement")
            print("4. Logout")#exits the loop

            choice = input("Choose: ")

            if choice == "1":
                for issue in self.issue_manager.issues:
                    print(issue)

            elif choice == "2":
                try:
                    issue_id = int(input("Issue ID: "))
                    status = input("New Status: ")
                    self.issue_manager.update_issue_status(issue_id, status)
                except ValueError:
                    print("Invalid ID.")

            elif choice == "3":
                msg = input("Announcement message: ").strip()
                if msg:
                    self.announcement_manager.add_announcement(
                        msg, self.user["username"]
                    )
                else:
                    print("Message cannot be empty.")

            elif choice == "4":
                break
            else:
                print("Invalid choice.")
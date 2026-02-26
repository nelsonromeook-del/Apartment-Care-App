from data_manager import DataManager

class Announcement:
    def __init__(self, message, posted_by):
        self.message = message
        self.posted_by = posted_by

    def display(self):
        print(f"\n{self.posted_by} says:")
        print(f"  {self.message}")


class AnnouncementManager(Announcement):
    FILE = "Data/announcements.json"

    def __init__(self):
        data = DataManager.read_file(self.FILE)
        self.announcements = data if data else []

    def add_announcement(self, message, posted_by):
        if not message.strip():
            print("Please write a message before posting.")
            return
        self.announcements.append({"message": message, "posted_by": posted_by})
        DataManager.write_file(self.FILE, self.announcements)
        print("Your announcement has been posted!")

    def view_announcements(self):
        if not self.announcements:
            print("No announcements yet.")
            return
        print("\n--- Announcements ---")
        for announcement in self.announcements:
            print(f"\n{announcement['posted_by']} says: {announcement['message']}")
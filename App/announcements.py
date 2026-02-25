#This file enables the admin to post announcements to all
from data_manager import DataManager


class Announcement:
    def __init__(self, message, posted_by):
        self.message = message
        self.posted_by = posted_by

    def to_dict(self):
        return {
            "message": self.message,
            "posted_by": self.posted_by
        }


class AnnouncementManager:
    FILE = "data/announcements.json"

    def __init__(self):
        # Load announcements when the object is created
        self.announcements = DataManager.read_file(self.FILE)

    def add_announcement(self, message, posted_by):
        new_announcement = Announcement(message, posted_by)
        self.announcements.append(new_announcement.to_dict())
        DataManager.write_file(self.FILE, self.announcements)
        print("Announcement added successfully.")

    def view_announcements(self):
        if not self.announcements:
            print("No announcements available.")
            return

        for announcement in self.announcements:
            print("\nPosted By:", announcement["posted_by"])
            print("Message:", announcement["message"])
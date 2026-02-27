# ApartmentCare CLI Application

A Python-based **Command-Line Interface (CLI)** tool for managing apartments, tenants, and administrative tasks.  
Tenants can report issues and view announcements, while admins can manage issues, post announcements, and update their status. All data is persisted in JSON files.

---

## Features

### Tenant
- View announcements posted by the admin.
- Report issues related to their apartment/house.
- View the status of previously reported issues.

### Admin
- View all reported issues.
- Update the status of any issue (e.g., Pending, Resolved).
- Post announcements to tenants.
- Activity logging of issues and announcements.

### General
- User authentication with role-based access (tenant/admin).
- Passwords are hashed with **SHA-256**.
- Persistent data stored in JSON files (`Data/` folder).
- Logs activity in `activity.log`.

---

## Folder Structure
ApartmentCare-App/
│
├── App/
│ ├── main.py # Application entry point
│ ├── auth.py # User authentication
│ ├── menu.py # CLI menu for tenants/admin
│ ├── issues.py # Issue management
│ ├── announcements.py # Announcements management
│ ├── data_manager.py # JSON file read/write utility
│ └── decorators.py # Logging decorator
│
├── Data/
│ ├── users.json
│ ├── issues.json
│ └── announcements.json
│
├── activity.log # Activity log of system events
├── requirements.txt
└── README.md


---

## Installation

1. Clone the repository:
```bash
git clone [link](https://github.com/nelsonromeook-del/Apartment-Care-App.git)
cd ApartmentCare-App/App

2. Usage(Bash)
`` Run python main.py
#this file enables users to post issues to the admin.
class Issue:
    def __init__(self,issue_id,house,description,status="Pending"):
        self._issue_id = issue_id
        self._house = house
        self._description = description
        self._status = status
    
    @property
    def id(self):
        return self._issue_id
    
    @property
    def house(self):
        return self._house

    @property
    def description(self):
        return self._description
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, new_status):
        self._status = new_status
    
    def to_dict(self):
        return {
            "id":self.id,
            "house": self.house,
            "description":self.description,
            "status":self.status
        }

class IssueManager:
    def __init__(self):
        self.storage = DataManager("data/issues.json")
        self._issues = self._load_issues()
    
    def _load_issues(self):
        tenant_data =self.storage.load()
        return [
            Issue(i["id"], i["house"], i["description"], i["status"])
            for i in tenant_data
        ]
    
    def save_issues(self):
        self.storage.save([issue.to_dict() for issue in self._issues])

    @property
    def issues(self):
        return self._issues
    
    @log_event("New issue reported")
    def report_issue(self, house, description):
        issue_id = len(self._issues) + 1
        new_issue = Issue(issue_id, house, description)
        self._issues.append(new_issue)
        self._save_issues()

    @log_event("Issue status updated")
    def update_issue_status(self, issue_id, new_status):
        for issue in self._issues:
            if issue.id == issue_id:
                issue.status = new_status
                self._save_issues()
                return True
        return False
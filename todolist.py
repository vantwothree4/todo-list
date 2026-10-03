from datetime import datetime

class Task:
    def __init__(self, title):
        self.title = title
        self.created_at = datetime.now()
        self.is_completed = False

    def changeStatus(self):
        self.is_completed = not self.is_completed

    def __str__(self):
        if self.is_completed:
            status = "✔"
        else:
            status = "✘"
        return f"{status} {self.title} | {self.created_at} "



        
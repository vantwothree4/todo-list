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


class TaskManager:
    def __init__(self):
        self.tasks = []

    def addTask(self,title):
        new_task = Task(title)
        self.tasks.append(new_task)

    def editTask(self, task_number, new_title):
        try:
            self.tasks[task_number - 1].title = new_title
        except IndexError:
            print("Task not found.")

    def deleteTask(self, task_number):
        try:
            self.tasks.pop(task_number - 1)
        except IndexError:
            print("Task not found.")

    def searchTask(self, keyword):
        result = []
        for task in self.tasks:
            if keyword.lower() in task.title.lower():
                result.append(task)
        return result

    def sortByDate(self):
        self.tasks.sort(key=lambda task: task.created_at, reverse=True)

    def changeTaskStatus(self, task_number):
        try:
            self.tasks[task_number - 1].changeStatus()
        except IndexError:
            print("Task not found.")
    

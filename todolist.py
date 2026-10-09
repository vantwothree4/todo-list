from datetime import datetime
import json

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
    
    def convertToDict(self):
        task_dictionary = { 
                "title": self.title, 
                "created_at" : self.created_at.isoformat(),
                "is_completed": self.is_completed 
            }
        return task_dictionary
    
    @classmethod
    def convertFromDict(cls, task_dictionary):
        task = cls(task_dictionary["title"])
        task.created_at = datetime.fromisoformat(task_dictionary["created_at"])
        task.is_completed = task_dictionary["is_completed"]
        return task
    
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.loadTasks()

    def addTask(self,title):
        new_task = Task(title)
        self.tasks.append(new_task)
        self.saveTasks()

    def editTask(self, task_number, new_title):
        try:
            self.tasks[task_number - 1].title = new_title
            self.saveTasks()
        except IndexError:
            print("Task not found.")

    def deleteTask(self, task_number):
        try:
            self.tasks.pop(task_number - 1)
            self.saveTasks()
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
        self.saveTasks()
        
    def changeTaskStatus(self, task_number):
        try:
            self.tasks[task_number - 1].changeStatus()
            self.saveTasks()
        except IndexError:
            print("Task not found.")

    def saveTasks(self):
        tasks_data = []
        for task in self.tasks:
            tasks_data.append(task.convertToDict())
        with open("tasks.json", "w") as file:
            json.dump(tasks_data, file, indent=4)
    def loadTasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks_data = json.load(file)
            for task_dictionary in tasks_data:
                task = Task.convertFromDict(task_dictionary)
                self.tasks.append(task)
        except FileNotFoundError:
            self.tasks = []
    
class Interface:
    def __init__(self):
        self.task_manager = TaskManager()

    def showMenu(self):
        print("\n\tTODO LIST") 
        print("1. Show tasks") 
        print("2. add task") 
        print("3. Edit task") 
        print("4. Delete task") 
        print("5. Search task") 
        print("6. Change task status") 
        print("7. Sort tasks") 
        print("0. Exit")

    def showTasks(self):
        print()
        if not self.task_manager.tasks:
            print("No tasks found.")
            return
        for number, task in enumerate(self.task_manager.tasks, start=1):
            print(f"{number}. {task}")

    def addTask(self):
        title = input("Enter task title: ") 
        self.task_manager.addTask(title) 

    def editTask(self): 
        try:
            task_number = int(input("Enter task number: ")) 
            new_title = input("Enter new title: ") 
            self.task_manager.editTask(task_number, new_title)
        except ValueError:
            print("Please enter a valid number.")

    def deleteTask(self): 
        try:
            task_number = int(input("Enter task number: ")) 
            self.task_manager.deleteTask(task_number)
        except ValueError:
            print("Please enter a valid number.")

    def searchTask(self): 
        keyword = input("Enter keyword: ") 
        results = self.task_manager.searchTask(keyword) 
        if not results:
            print("No matching tasks found.")
            return
        for number, task in enumerate(results, start=1): 
            print(f"{number}. {task}")

    def changeTaskStatus(self): 
        try:
            task_number = int(input("Enter task number: ")) 
            self.task_manager.changeTaskStatus(task_number) 
        except ValueError:
            print("Please enter a valid number.")

    def sortTasks(self): 
        self.task_manager.sortByDate() 
        self.showTasks()

    def run(self): 
        while True: 
            self.showMenu() 
            choice = input("Choose an option: ") 
            if choice == "1": 
                self.showTasks() 
            elif choice == "2": 
                self.addTask() 
            elif choice == "3": 
                self.editTask() 
            elif choice == "4": 
                self.deleteTask() 
            elif choice == "5": 
                self.searchTask() 
            elif choice == "6": 
                self.changeTaskStatus() 
            elif choice == "7": 
                self.sortTasks() 
            elif choice == "0": 
                print("Goodbye!") 
                break 
            else: 
                print("Invalid option.")

interface = Interface()
interface.run()


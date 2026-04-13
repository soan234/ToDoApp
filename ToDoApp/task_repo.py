from task import Task

class TaskRepo:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].done = True

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def get_all(self):
        return self.tasks
    

    
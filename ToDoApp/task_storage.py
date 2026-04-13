from task import Task

class FileStorage:
    def __init__(self, filename = 'todotasks.txt'):
        self.filename = filename
    
    def save(self, tasks):
        with open(self.filename, "w") as filename:
            for task in tasks:
                filename.write(f"{task.title}||{task.done}\n")


    def load(self):
        tasks = []
        try:
            with open(self.filename, 'r') as filename:
                for line in filename:
                    title, done = line.strip().split("||")
                    tasks.append(Task(title, done == "True"))
        except FileNotFoundError:
            pass
        return tasks
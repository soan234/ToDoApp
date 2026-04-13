from task import Task

class ToDoApp:
    def __init__(self, repo, storage):
        self.repo = repo
        self.storage = storage
        self.repo.tasks = self.storage.load()

    def add_task(self, title):
        self.repo.add_task(Task(title))
        self.storage.save(self.repo.get_all())

    def mark_done(self, index):
        self.repo.mark_done(index)
        self.storage.save(self.repo.get_all())

    def delete_task(self, index):
        self.repo.delete_task(index)
        self.storage.save(self.repo.get_all())

    def get_tasks(self):
        return self.rep.get_all()
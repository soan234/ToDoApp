import unittest
import os
from task import Task
from task_repo import TaskRepo
from task_storage import FileStorage
from todoapp import ToDoApp

class TestApp(unittest.TestCase):

    def setUp(self):
        #körs före varje test, skapar en tom arbetsfil och en ny app-instans
        self.testfile = 'testapp.txt'

        if os.path.exists(self.testfile):
            os.remove(self.testfile)

        self.repo = TaskRepo()
        self.storage = FileStorage(self.testfile)
        self.app = ToDoApp(self.repo, self.storage)

    def tearDown(self):
        #Körs efter varje test och städar bort testfilen
        if os.path.exists(self.testfile):
            os.remove(self.testfile)

    def test_add_task(self):
        #testar att lägga till en uppgift via appen
        self.app.add_task("Hänga tvätt")
        self.assertEqual(self.repo.get_all()[0].title, "Hänga tvätt")

    def test_mark_done(self):
        #testar att markera en uppgift som klar
        self.app.add_task("Handla")
        self.app.mark_done(0)
        self.assertTrue(self.repo.get_all()[0].done)

    def test_delete_task(self):
        #testar att ta bort en uppgift
        self.app.add_task("Ta bort uppgift")
        self.app.delete_task(0)
        self.assertEqual(len(self.repo.get_all()), 0)

if __name__ == "__main__":
    unittest.main()

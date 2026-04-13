import unittest
from task import Task
from task_repo import TaskRepo

class TestTaskRepo(unittest.TestCase):

    def setUp(self):
        self.repo = TaskRepo()

    def test_add_task(self):
        self.repo.add_task(Task("Handla smör"))
        self.assertEqual(len(self.repo.get_all()), 1)
        self.assertEqual(self.repo.get_all()[0].title, "Handla smör")

    def test_mark_done(self):
        self.repo.add_task(Task("Testa om klart"))
        self.repo.mark_done(0)
        self.assertTrue(self.repo.get_all()[0].done)

    def test_delete_task(self):
        self.repo.add_task(Task("Ta bort uppgift"))
        self.repo.delete_task(0)
        self.assertEqual(len(self.repo.get_all()), 0)

    def test_invalid_done(self):
        self.repo.add_task(Task("Boka tandläkartid"))
        self.repo.mark_done(76)
        self.assertFalse(self.repo.get_all()[0].done)

    def test_invalid_delete(self):
        self.repo.add_task(Task("Hyra bil"))
        self.repo.delete_task(5)
        self.assertEqual(len(self.repo.get_all()), 1)

if __name__ == "__main__":
    unittest.main()
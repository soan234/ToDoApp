import unittest
from task import Task
from task_repo import TaskRepo

class TestTaskRepo(unittest.TestCase):

    def setUp(self):
        #körs före varje test
        self.repo = TaskRepo()

    def test_add_task(self):
        #testar att lägga till en uppgift i repot
        self.repo.add_task(Task("Handla smör"))
        self.assertEqual(len(self.repo.get_all()), 1)
        self.assertEqual(self.repo.get_all()[0].title, "Handla smör")

    def test_mark_done(self):
        #testar att markera en uppgift som klar i repot
        self.repo.add_task(Task("Testa om klart"))
        self.repo.mark_done(0)
        self.assertTrue(self.repo.get_all()[0].done)

    def test_delete_task(self):
        #testar att ta bort en uppgift via index i repot
        self.repo.add_task(Task("Ta bort uppgift"))
        self.repo.delete_task(0)
        self.assertEqual(len(self.repo.get_all()), 0)

    def test_invalid_done(self):
        #testar att markea en ogiltig index som klar, detta ska inte krascha
        self.repo.add_task(Task("Boka tandläkartid"))
        self.repo.mark_done(76)
        self.assertFalse(self.repo.get_all()[0].done)

    def test_invalid_delete(self):
        #testar att ta bort en uppgift med ogiltig index
        self.repo.add_task(Task("Hyra bil"))
        self.repo.delete_task(5)
        self.assertEqual(len(self.repo.get_all()), 1)

if __name__ == "__main__":
    unittest.main()

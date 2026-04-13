import unittest
from task import Task

class TestTask(unittest.TestCase):
    def test_add_task(self):
        task = Task ("Posta brev")
        self.assertEqual(task.title, "Posta brev")
        self.assertFalse(task.done)

    def test_mark_done(self):
        task = Task("Hänga tvätt", done=True)
        self.assertTrue(task.done)

    if __name__== "__main__":
        unittest.main()


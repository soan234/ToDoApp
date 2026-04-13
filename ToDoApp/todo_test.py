import unittest
import json
from todo import add_task, mark_done, delete_task, get_tasks, tasks

class TestTodo(unittest.TestCase):
    def setUp(self):
        tasks.clear()

    def test_add_task(self):
        add_task("Slänga sopor")
        self.assertEqual(len(get_tasks()), 1)
        self.assertEqual(get_tasks()[0]["title"], "Slänga sopor")
        self.assertFalse(get_tasks()[0]["done"])

    def test_mark_done(self):
        add_task("Testa uppgift klar")
        mark_done(0)
        self.assertTrue(get_tasks()[0]["done"])

    def test_delete_task(self):
        add_task("Testa ta bort")
        delete_task(0)
        self.assertEqual(len(get_tasks()), 0)


    def test_done_invalid_index(self):
        add_task("Hänga tvätt")

        mark_done(47)
        self.assertFalse(get_tasks()[0]["done"])


    def test_delete_invalid_index(self):
        add_task("Handla")

        delete_task(78)

        self.assertEqual(len(get_tasks()),1)

    
    def test_more_tasks(self):
        add_task("Boka tid hos tandläkare")
        add_task("Posta brev")

        self.assertEqual(len(get_tasks()), 2)
        
if __name__ == "__main__":
    unittest.main()
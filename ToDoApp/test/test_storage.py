import unittest
from unittest.mock import mock_open, patch
from task import Task
from task_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def test_save(self):
        storage = FileStorage('todotasks.txt')
        tasks = [Task("Hänga tvätt", False)]

        mock = mock_open()
        with patch('builtins.open', mock):
            storage.save(tasks)

        mock.assert_called_once_with('todotasks.txt', 'w')
        handle = mock()
        handle.write.assert_called_once_with("Hänga tvätt||False\n")

    def test_load(self):
        fake_file = "Hänga tvätt||False\n"
        storage = FileStorage('todotasks.txt')

        with patch('builtins.open', mock_open(read_data=fake_file)):
            tasks = storage.load()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Hänga tvätt")
        self.assertFalse(tasks[0].done)

if __name__ == "__main__":
    unittest.main()


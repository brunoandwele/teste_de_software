from unittest import TestCase

from aula_03 import TaskManager

class TestTaskManeger(TestCase):
    def test_add_number(self):
        tk = TaskManager()
        
        self.assertEqual(tk.add_task(1), "Número como task")

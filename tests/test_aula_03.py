from unittest import TestCase

from src import aula_03

class TestTaskManeger(TestCase):
    def test_add_number(self):
        tk = aula_03.TaskManager()
        
        self.assertEqual(tk.add_task(1), "Número como task")

from datetime import datetime
from unittest import TestCase

from app.todo import Todo


class TodoTest(TestCase):
    def test_complete_should_mark_as_complete(self):
        todo = Todo('text', datetime.now())
        self.assertFalse(todo.is_completed)

        todo.complete()
        self.assertEqual(todo.is_completed, True)

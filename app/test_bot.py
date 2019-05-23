from datetime import datetime
from unittest import TestCase

from app.bot import Bot
from app.todo import Todo


class BotTestCase(TestCase):
    def test_show_items_should_display_text_when_list_is_empty(self):
        bot = Bot()
        result = bot.show_items()
        self.assertEqual(result, 'Список пуст')

    def test_show_items_should_display_list_of_todo(self):
        bot = Bot()
        bot.todos.append(Todo('Тест 1', datetime.now()))
        bot.todos.append(Todo('Тест 2', datetime.now()))

        result = bot.show_items()
        self.assertEqual(result, 'Тест 1\nТест 2')



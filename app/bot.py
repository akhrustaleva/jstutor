class Bot:
    def __init__(self):
        self.todos = []

    def add_item(self):
        pass

    def complete_item(self):
        pass

    def show_items(self):
        if len(self.todos) == 0:
            return "Список пуст"

        return '\n'.join([str(todo) for todo in self.todos])






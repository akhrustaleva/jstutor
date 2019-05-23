class Todo:
    def __init__(self, text, scheduled_at, is_completed=False):
        self.text = text
        self.scheduled_at = scheduled_at
        self.is_completed = is_completed

    def complete(self):
        self.is_completed = True

    def __str__(self):
        return self.text

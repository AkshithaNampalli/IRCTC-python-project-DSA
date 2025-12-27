


class BookingStack:
    def __init__(self):
        self.stack = []

    def push(self, record):
        self.stack.append(record)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def history(self):
        return self.stack

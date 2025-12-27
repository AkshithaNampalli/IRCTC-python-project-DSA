


from collections import deque

class BookingQueue:
    def __init__(self):
        self.queue = deque()

    def add(self, passenger):
        self.queue.append(passenger)

    def get(self):
        return self.queue.popleft() if self.queue else None

    def is_empty(self):
        return len(self.queue) == 0

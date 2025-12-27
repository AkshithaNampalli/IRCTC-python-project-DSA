

from collections import deque

class WaitingList:
    def __init__(self):
        self.deque = deque()

    # Add passenger based on type
    def add(self, passenger_name, ticket_type):
        if ticket_type.lower() == "tatkal":
            self.deque.appendleft(passenger_name)   # LEFT
        else:
            self.deque.append(passenger_name)       # RIGHT

    # Allocate seat from LEFT
    def allocate(self):
        if self.deque:
            return self.deque.popleft()
        return None

    def is_empty(self):
        return len(self.deque) == 0

    def show(self):
        return list(self.deque)

from seat_tree import SeatTree
from booking_queue import BookingQueue
from waiting_list import WaitingList
from booking_stack import BookingStack


class Controller:
    def __init__(self):
        self.trains = {
            "12345": SeatTree(2),
            "54321": SeatTree(5)
        }
        self.queue = BookingQueue()
        self.waiting = WaitingList()      # one waiting list (simplified model)
        self.stack = BookingStack()

    # 1️⃣ View trains
    def view_trains(self):
        for tid, tree in self.trains.items():
            total = tree.count_available() + self._count_booked(tree)
            available = tree.count_available()
            print(f"Train {tid} : {available}/{total} seats available")

    def _count_booked(self, tree):
        # helper for total seats
        return tree._count(tree.root) - tree.count_available()

    # 2️⃣ Book ticket
    def book_ticket(self):
        tid = input("Enter Train Number: ")
        if tid not in self.trains:
            print("Invalid Train Number")
            return

        ttype = input("Ticket Type (Tatkal/Normal): ")
        n = int(input("Enter number of passengers: "))

        tree = self.trains[tid]
        available = tree.count_available()

        for i in range(n):
            name = input(f"Enter Passenger Name {i+1}: ")

            if available > 0:
                self.queue.add(name)
                passenger = self.queue.get()
                seat = tree.allocate_seat(passenger)
                self.stack.push((tid, passenger, seat))
                print(f"{passenger} allotted Seat {seat} in Train {tid}")
                available -= 1
            else:
                self.waiting.add(name, ttype)
                print(f"{name} added to Waiting List ({ttype})")

    # 3️⃣ Cancel ticket
    def cancel_ticket(self):
        record = self.stack.pop()
        if not record:
            print("No bookings to cancel")
            return

        tid, name, seat = record
        self.trains[tid].free_seat(seat)
        print(f"Cancelled {name}'s ticket | Train {tid} | Seat {seat} freed")

        next_passenger = self.waiting.allocate()
        if next_passenger:
            new_seat = self.trains[tid].allocate_seat(next_passenger)
            self.stack.push((tid, next_passenger, new_seat))
            print(f"Waiting passenger {next_passenger} allotted Seat {new_seat}")
        else:
            print("Waiting list empty. No allocation.")

    # 4️⃣ View Waiting List
    def view_waiting_list(self, tid):
        if tid not in self.trains:
            print("Invalid Train Number")
            return

        wl = self.waiting.show()
        if not wl:
            print(f"Waiting list for Train {tid} is empty")
        else:
            print(f"Waiting list for Train {tid}:")
            for idx, name in enumerate(wl, start=1):
                print(f"{idx}. {name}")

    # 5️⃣ Admin Reports
    def admin_report(self):
        tid = input("Enter Train Number for Admin Report: ")
        if tid not in self.trains:
            print("Invalid Train Number")
            return

        tree = self.trains[tid]

        print("\nAdmin Seat Traversals")
        print("1. Preorder")
        print("2. Inorder")
        print("3. Postorder")
        print("4. Level Order")

        ch = input("Choose traversal: ")

        if ch == "1":
            result = tree.preorder()
        elif ch == "2":
            result = tree.inorder()
        elif ch == "3":
            result = tree.postorder()
        elif ch == "4":
            result = tree.level_order()
        else:
            print("Invalid choice")
            return

        print("\nSeat No | Passenger")
        for seat, passenger in result:
            print(f"{seat}      | {passenger if passenger else 'None'}")

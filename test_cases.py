from controller import Controller

c = Controller()

print("TEST CASE 1: Tatkal Booking")
c.book_ticket()

print("TEST CASE 2: Normal Booking")
c.book_ticket()

print("TEST CASE 3: Seat Full → Waiting List")
c.book_ticket()
c.book_ticket()
c.book_ticket()

print("TEST CASE 4: Cancellation & Promotion")
c.cancel_ticket()

print("TEST CASE 5: Admin Report")
c.admin_report()

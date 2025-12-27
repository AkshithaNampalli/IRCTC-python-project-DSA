


from controller import Controller

def menu():
    print("\n=== IRCTC Backend System ===")
    print("1. View Available Trains")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. View Waiting List")
    print("5. Admin Reports")
    print("0. Exit")

def main():
    c = Controller()
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            c.view_trains()
        elif choice == "2":
            c.book_ticket()
        elif choice == "3":
            c.cancel_ticket()
        elif choice == "4":
            tid = input("Enter Train Number: ")
            c.view_waiting_list(tid)
        elif choice == "5":
            c.admin_report()
        elif choice == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

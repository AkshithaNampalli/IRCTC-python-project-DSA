# IRCTC-python-project-DSA
🚆 IRCTC Backend System (Python Mini Project) 📌 Project Overview

This project is a simplified backend simulation of IRCTC ticket booking implemented using core Data Structures in Python.

It demonstrates how Trees, Queue, Stack, Deque, BFS, and DFS work together in a real-world scenario like railway seat booking.

The system supports:

Viewing available trains & seats

Booking multiple tickets (Normal / Tatkal)

Priority-based waiting list

Ticket cancellation

Administrative seat allocation reports using tree traversals

🎯 Project Objectives

Apply multiple Data Structures in one system

Demonstrate seat allocation logic

Handle waiting list with priority

Support seat cancellation and rearrangement

Provide Admin views using DFS & BFS

🧠 Data Structures Used Feature Data Structure Seat Storage Binary Tree Seat Allocation DFS Admin Reports DFS (Pre/In/Post) Level Order View BFS Booking Order Queue Waiting List Deque Cancellation Stack

📁 Project Structure IRCTC_Python-project/ │ ├── main.py ├── controller.py ├── seat_tree.py ├── booking_queue.py ├── waiting_list.py ├── booking_stack.py ├── README.md

📄 File-wise Explanation 1️⃣ main.py

Purpose: Entry point of the application.

Displays menu

Accepts user input

Calls controller methods

Menu Options

View Available Trains
Book Ticket
Cancel Ticket
Admin Reports
View Waiting List
Exit
2️⃣ controller.py

Purpose: Central logic handler.

Handles:

Train validation

Booking logic

Cancellation logic

Waiting list allocation

Admin traversal reports

📌 This file connects all data structures together.

3️⃣ seat_tree.py

Purpose: Seat management using Binary Tree

Each node represents: Seat Number Passenger Name Booking Status Functions Allocate seat (DFS) Free seat Count available seats

Traversals:

Preorder , Inorder, Postorder, Level Order (BFS)

Admin sees:

Seat No | Passenger Name / None

4️⃣ booking_queue.py

Purpose: Manage booking order

FIFO seat allocation

Ensures first passenger gets seat first

Used when seats are available.

5️⃣ waiting_list.py

Purpose: Priority waiting list using Deque

Rules

Tatkal → Add to LEFT

Normal → Add to RIGHT

Allocation always from LEFT

📌 Demonstrates priority handling

6️⃣ booking_stack.py

Purpose: Handle cancellation

LIFO behavior

Last booked ticket cancelled first

Ensures correct seat restoration

🔄 Booking Flow (Step-by-Step)

User selects Book Ticket

Enter:

Train Number

Ticket Type (Tatkal / Normal)

Number of Passengers

Passenger Names

If seats available:

Queue → Seat Tree → Stack

If full:

Deque → Waiting List

❌ Cancellation Flow

Last booked ticket popped from Stack

Seat freed in Seat Tree

Waiting list checked

If available:

Passenger promoted

Seat re-allocated

👨‍💼 Admin Reports

Admin can view seat allocation using:

Preorder Traversal (DFS)

Inorder Traversal (DFS)

Postorder Traversal (DFS)

Level Order Traversal (BFS)

Output Format

Seat No | Passenger 1 | Akash 2 | None

▶️ How to Execute the Project 🔹 Step 1: Open Terminal cd IRCTC_Python-project

🔹 Step 2: Run the Program python main.py

✔ Cancellation Test

Cancel last booking

Waiting passenger promoted

Seat reassigned

About
No description, website, or topics provided.
Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 0 watching
Forks
 0 forks
Report repository
Releases
No releases published
Packages
No packages published
Footer

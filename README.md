Library Management System

Project Overview : The Library Management System is a command-line-based application developed using Python that helps manage library operations effectively. The system allows users to perform tasks like adding, borrowing, and returning books, managing user and author information, and even tracking overdue fines and reservations.

This project demonstrates the application of Object-Oriented Programming (OOP) principles, including encapsulation, modular design, and error handling. The code is modular, well-structured, and includes optional bonus features like fine calculations and a reservation system.

Features

1. Book Operations

• Add new books with details like title, author, genre, and availability status.

• Borrow and return books, with automatic updates to their status.

• Search for books by title and display book details.

• Reserve unavailable books and get notified when they are returned.

• Display a list of all books in the library.

2. User Operations

• Add new users with details like name and library ID.

• View user details, including borrowed books and outstanding fines.

• Display a list of all users.

• Pay overdue fines directly from the system.

3. Author Operations

• Add new authors with information like name and biography.

• View author details.

• Display a list of all authors.

4. Fine Calculation (Bonus)

• Automatically calculate fines for overdue books using the datetime module.

• Allow users to pay fines and update their account balances.

5. Reservation System (Bonus)

• Enable users to reserve unavailable books.

• Notify users when a reserved book becomes available.

Screenshots

Main Menu
Welcome to the Library Management System!
Main Menu:

1. Book Operations

2. User Operations

3. Author Operations

4. Quit

Book Operations
Book Operations:

1. Add a new book

2. Borrow a book

3. Return a book

4. Search for a book

5. Display all books

6. Back to Main Menu

User Operations
User Operations:

1. Add a new user

2. View user details

3. Display all users

4. Pay fines

5. Back to Main Menu

Instructions to Run the Application
Prerequisites

1. Install Python 3.7 or later.

2. Ensure you have a terminal or command prompt to run Python scripts.

Setup

1. Clone the repository:
git clone https://github.com/your-username/library-management-system.git cd library-management-system

2. Install any required libraries 

3. Run the main script:

python Library_Management_System.py


Using the Application

• Follow the on-screen prompts to navigate through the menus.

• Use numeric options to perform operations like adding books, borrowing books, or managing users.

Directory Structure

library-management-system/

│

├── books.py               # Book-related classes and operations

├── users.py               # User-related classes and operations

├── authors.py             # Author-related classes and operations

├── main.py                # Main entry point for the application

├── requirements.txt       # Required libraries (if applicable)

├── README.md              # Documentation

└── data/                  # Text files for saving data (optional)

    ├── books.txt

    ├── users.txt

    └── authors.txt


Error Handling

• The application includes input validation to handle invalid inputs gracefully.

• Common issues, such as entering incorrect book titles or invalid menu options, are managed using try-except blocks.

Optional Features
Text File Handling

• Data is saved in text files (books.txt, users.txt, authors.txt) for persistence.

• Data is loaded from these files when the application starts.

Fine Calculation

• Fines are calculated for overdue books at $1 per day past the due date.

• Users can pay fines directly from the system.


Reservation System

• Users can reserve books that are currently unavailable.

• Notifications are displayed when reserved books become available.


Future Enhancements

• Implement a graphical user interface (GUI) for better usability.

• Add support for database integration (e.g., SQLite or MySQL) for larger-scale applications.

• Extend features to include genre management or advanced book filtering.


link to your GitHub repository in your project documentation 




#  LibraryManagementSystem/

# Class Structure

# 1. Book Class

class Book:
    def __init__(self, title, author, genre, pub_date, availability=True):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__pub_date = pub_date
        self.__availability = availability

            # Getters and setters
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__availability

    def borrow(self):
        if self.__availability:
            self.__availability = False
            return True
        return False

    def return_book(self):
        self.__availability = True

#  2. User Class

class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_user_details(self):
        return {
            "Name": self.__name,
            "Library ID": self.__library_id,
            "Borrowed Books": self.__borrowed_books
        }

    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)

#  3. Author Class

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_author_details(self):
        return {
            "Name": self.__name,
            "Biography": self.__biography
        }
    
#  Menu System

#  Main Menu (menus.py)
def user_menu():
    print("user menu logic will go here.")

def author_menu():
    print("Auther menu logic will go here.")

def main_menu():
    while True:
        print("\nWelcome to the Library Management System!")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '1':
            book_menu()
        elif choice == '2':
            user_menu()
        elif choice == '3':
            author_menu()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Book Menu
def add_new_book():
    print("Functionality to add a new book will go here ")

def borrow_book():
    print("Functionality to borrow a new book will go here ")

def return_book():
    print("Functionality to return a new book will go here ")

def search_book():
    print("Functionality to search a new book will go here ")

def display_books():
    print("Functionality to display a new book will go here ")

def book_menu():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_new_book()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            display_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

# Error Handling

def input_with_validation(prompt, regex):
    import re
    while True:
        try:
            user_input = input(prompt)
            if re.match(regex, user_input):
                return user_input
            else:
                raise ValueError("Invalid input format.")
        except ValueError as e:
            print(e)

# Text File Handling (Bonus)

def load_books_from_file(file_path):
    books = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                title, author, genre, pub_date, availability = line.strip().split('|')
                books.append(Book(title, author, genre, pub_date, availability == 'True'))
    except FileNotFoundError:
        print("Books file not found. Starting with an empty library.")
    return books

def save_books_to_file(file_path, books):
    with open(file_path, 'w') as file:
        for book in books:
            file.write(f"{book.get_title()}|{book.get_author()}|{book.get_genre()}|"
                       f"{book.get_pub_date()}|{book.is_available()}\n")

# Optional Bonus Features

 #  1. Reservation System

from datetime import datetime 

class Book: 
    def __init__(self, title, author, genre, pub_date, availability=True): 
        self.__title = title 
        self.__author = author 
        self.__genre = genre 
        self.__pub_date = pub_date 
        self.__availability = availability 
        self.__reserved_by = None  # Initially, no one has reserved the book. 

        def reserve(self, user_id): 
            if not self.__availability and self.__reserved_by is None: 
                self.__reserved_by = user_id 
                return True 
            return False 
        
        def notify_reservation(self): 
            if self.__reserved_by: 
                print(f"Notification: Book '{self.__title}' is now available for user ID: {self.__reserved_by}") 
                self.__reserved_by = None  # Clear the reservation. 

        # Modify the return_book method to notify the user if the book was reserved 
        def return_book(self): 
            self.__availability = True 
            if self.__reserved_by: 
                self.notify_reservation()


# • Add a reserved_by attribute to the Book class.

def reserve_book(books, user_id): 
    title = input("Enter the title of the book to reserve: ") 
    for book in books: 
        if book.get_title().lower() == title.lower(): 
            if book.is_available(): 
                print(f"Book '{title}' is available. You can borrow it directly.") 
            elif book.reserve(user_id): 
                print(f"Book '{title}' has been reserved for you. You will be notified when it becomes available.") 
            else: 
                print(f"Book '{title}' is already reserved by another user.") 
            return 
        print("Book not found.")

# • Notify users when their reserved book becomes available.

def return_book(books): 
    title = input("Enter the title of the book to return: ") 
    for book in books: 
        if book.get_title().lower() == title.lower(): book.return_book() 
        print(f"Book '{title}' has been returned.") 
        return 
    print("Book not found.")

# 2. Fine Calculation

from datetime import datetime, timedelta 

class User: 
    def __init__(self, name, library_id): 
        self.__name = name 
        self.__library_id = library_id 
        self.__borrowed_books = {} 
        self.__fine_balance = 0.0 
    def borrow_book(self, book_title): 
        due_date = datetime.now() + timedelta(days=14) # 14 days to return 
        self.__borrowed_books[book_title] = due_date 
    
    def return_book(self, book_title): 
            if book_title in self.__borrowed_books: 
                due_date = self.__borrowed_books.pop(book_title) 
                if datetime.now() > due_date: 
                    days_overdue = (datetime.now() - due_date).days 
                    fine = days_overdue * 1.0 # Assume $1 per day overdue 
                    self.__fine_balance += fine 
                    print(f"Book returned late. Fine of ${fine:.2f} added to your account.") 
                else: 
                    print("Book returned on time.") 
            else: 
                print("You haven't borrowed this book.") 
    def pay_fine(self, amount): 
        if amount <= self.__fine_balance: 
            self.__fine_balance -= amount 
            print(f"Fine of ${amount:.2f} paid. Remaining balance: ${self.__fine_balance:.2f}") 
        else: 
            print("Amount exceeds fine balance.") 
    def get_fine_balance(self): 
        return self.__fine_balance

# 3. Use the datetime module to calculate overdue fines based on due dates.

def display_overdue_books(users): 
    print("Overdue Books:") 
    for user in users: 
        user_details = user.get_user_details() 
        for book, due_date in user_details["Borrowed Books"].items(): 
            if datetime.now() > due_date: 
                days_overdue = (datetime.now() - due_date).days 
                fine = days_overdue * 1.0 # Assume $1 per day overdue 
                print(f"User: {user_details['Name']}, Book: {book}, Days Overdue: {days_overdue}, Fine: ${fine:.2f}")


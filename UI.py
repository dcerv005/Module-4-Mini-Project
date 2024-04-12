from book import Book
from user import User
user= User()
book= Book()
def opening_menu():
    pass

def book_operations():
    try:
        print("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
        option = int(input("Please pick an option to continue: "))
        if option not in [1, 2, 3, 4, 5]:
            raise ValueError("Invalid option. (1-5)")
        elif option == 1:
            title = input("What is the title: ").title()
            author = input("Who is the author? ").title()
            ISBN = int(input("What is the ISBN? "))
            genre = input("What is the genre? ").title()
            publication_date = input("What is the publication date? ")
            book.add_book(title, author, ISBN, genre, publication_date)
        elif option == 2:
            ISBN = int(input("Please enter the ISBN of the book you would like to borrow: "))
            library_ID = input("Please submit your login: ")                
            user.borrow_book(library_ID, book.borrow_book(ISBN))
        elif option == 3:
            library_ID= input("Please enter your library ID to return the book: ")
            ISBN = int(input("Please enter the ISBN of the book you would like to return: "))
            user.return_book(library_ID, book.return_book(ISBN))
        elif option == 4:
            int(input("Please enter the ISBN of the book you are looking for: "))
            book.search_book(ISBN)
        elif option == 5:
            book.display_books()
    except Exception as e:
        print(e)

def user_operations():
    try:
        print("\nUser Operations\n1. Add a new user\n2. View user details\n3. Display all users\n")
        option = int(input("Please pick an option to continue: "))
        if option not in [1, 2, 3]:
            raise ValueError("Invalid option. (1-3)")
        elif option == 1:
            library_ID= input("Please enter your new library ID: ")
            name = input("Please enter your name: ")
            user.add_user(library_ID, name)
        elif option == 2:
            library_ID = input("Please enter your library ID to get user information: ")
            user.user_info(library_ID)
        elif option == 3:
            user.display_users()
    except Exception as e:
        print(e)
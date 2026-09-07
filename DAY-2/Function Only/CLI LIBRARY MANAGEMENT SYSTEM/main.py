from books import add_book, remove_book, search_book
from users import register_user
from library import issue_book, return_book, list_available_books, list_issued_books
from validators import validate_id, validate_name, validate_text

def display_books(books):
    if not books:
        print("No books found")
        return

    for book in books:
        print("ID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])

        if book["available"]:
            print("Status: Available")
        else:
            print("Status: Issued to User", book["issued_to"])

        print()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add book")
    print("2. Remove book")
    print("3. Search book")
    print("4. Register user")
    print("5. Issue book")
    print("6. Return book")
    print("7. List available books")
    print("8. List issued books")
    print("9. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            book_id = validate_id(input("Enter book ID: "))
            title = validate_text(input("Enter book title: "), "Title")
            author = validate_text(input("Enter author name: "), "Author")

            print(add_book(book_id, title, author))

        elif choice == "2":
            book_id = validate_id(input("Enter book ID: "))

            print(remove_book(book_id))

        elif choice == "3":
            search = validate_text(input("Enter title or author: "), "Search")

            result = search_book(search)
            display_books(result)

        elif choice == "4":
            user_id = validate_id(input("Enter user ID: "))
            name = validate_name(input("Enter user name: "))

            print(register_user(user_id, name))

        elif choice == "5":
            book_id = validate_id(input("Enter book ID: "))
            user_id = validate_id(input("Enter user ID: "))

            print(issue_book(book_id, user_id))

        elif choice == "6":
            book_id = validate_id(input("Enter book ID: "))

            print(return_book(book_id))

        elif choice == "7":
            result = list_available_books()
            display_books(result)

        elif choice == "8":
            result = list_issued_books()
            display_books(result)

        elif choice == "9":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid menu choice")

    except ValueError as e:
        print("Error:", e)
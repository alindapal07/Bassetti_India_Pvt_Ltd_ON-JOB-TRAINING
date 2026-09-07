from books import books
from users import user_exists

def issue_book(book_id, user_id):
    if not user_exists(user_id):
        raise ValueError("User does not exist")

    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                raise ValueError("Book is already issued")

            book["available"] = False
            book["issued_to"] = user_id

            return "Book issued successfully"

    raise ValueError("Book not found")

def return_book(book_id):
    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                raise ValueError("Book is not issued")

            book["available"] = True
            del book["issued_to"]

            return "Book returned successfully"

    raise ValueError("Book not found")

def list_available_books():
    available = []

    for book in books:
        if book["available"]:
            available.append(book)

    return available

def list_issued_books():
    issued = []

    for book in books:
        if not book["available"]:
            issued.append(book)

    return issued
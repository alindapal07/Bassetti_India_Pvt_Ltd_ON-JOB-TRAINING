books = [
    {
        "id": 1,
        "title": "Inglorious Empire",
        "author": "Sashi Tharoor",
        "available": True
    }
]

def add_book(book_id, title, author):
    for book in books:
        if book["id"] == book_id:
            raise ValueError("Book ID already exists")

    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    })

    return "Book added successfully"

def remove_book(book_id):
    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                raise ValueError("Cannot remove an issued book")

            books.remove(book)
            return "Book removed successfully"

    raise ValueError("Book not found")

def search_book(search):
    result = []

    for book in books:
        if search.lower() in book["title"].lower() or search.lower() in book["author"].lower():
            result.append(book)

    return result
def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog:
        if book_id not in borrowed_books:
            borrowed_books.append(book_id)
            print(f"Book {book_id} borrowed.")
        else:
            print("Book already borrowed.")
    else:
        print("Book does not exist.")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned.")
    else:
        print("Book was not borrowed.")


def register_member(members, member_id):
    members.add(member_id)


def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            print(f"{book_id}: {details[0]} by {details[1]} ({details[2]})")


def main():
    catalog = {}
    borrowed_books = []
    members = set()

    # Adding 4 books
    add_book(catalog, 1, "Python Basics", "John", 2020)
    add_book(catalog, 2, "Data Science", "Alice", 2021)
    add_book(catalog, 3, "Machine Learning", "Bob", 2022)
    add_book(catalog, 4, "AI Fundamentals", "David", 2023)

    # Registering members
    register_member(members, 101)
    register_member(members, 102)
    register_member(members, 103)
    register_member(members, 101)  # Duplicate (ignored)

    # Borrowing books
    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 3)

    # Returning one book
    return_book(borrowed_books, 1)

    # Display available books
    show_available(catalog, borrowed_books)


if __name__ == "__main__":
    main()

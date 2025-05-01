library = [
    {
        "title": "The Road Ahead",
        "author": "Bill Gates",
        "isLoaned": True
    },
    {
        "title": "Steve Jobs",
        "author": "Walter Isaacson",
        "isLoaned": True
    },
    {
        "title": "Mockingjay: The Final Book of The Hunger Games",
        "author": "Suzanne Collins",
        "isLoaned": False
    }
]


def loan_status(lib):
    for book in lib:
        book_info = f"{book['title']} by {book['author']}"

        if book["isLoaned"]:
            print(f"Out on loan: {book_info}")
        else:
            print(f"On the shelf: {book_info}")


def get_books_by_author(library, author_name):
    books_by_author = []

    for book in library:
        if book["author"] == author_name:
            book_status = "Out on loan" if book["isLoaned"] else "On the shelf"
            books_by_author.append(f"{book['title']} - {book_status}")

    return books_by_author


def search_by_book_name(library, search_term):
    for book in library:
        if book["title"] == search_term:
            return True
    return False



def display_loan_totals():
    onloan = 0
    not_on_loan. = 0
    for book in library:
        if book["isLoaned"] == True:
            onloan += 1
        else:
            not_on_loan += 1
    return f"There is {onloan} on loan and {not_on_loan} not on loan"


def alter_book_status(book_title, new_status):
    for book in library:
        if book["title"] == book_title:
            book["isLoaned"] == new_status
            return library



def add_new_book(library, title, author, is_loaned):
    new_book = {"title": title,
    "author": author,
    "isLoaned": is_loaned}
    library.append(new_book)
    return library


def remove_book(library, book_title):
    for book in range(len(library)):
        if book[i]["title"] == book_title:
            library.pop(book)
            return library
    return 




# Example usage
author_name = "Suzanne Collins"
books_status = get_books_by_author(library, author_name)

print(f"Books by {author_name}:")
print(books_status)

loan_status(library)
# library.py

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, year):
        self.books[isbn] = {'title': title, 'author': author, 'year': year, 'available': True}

    def get_book(self, isbn):
        return self.books.get(isbn)

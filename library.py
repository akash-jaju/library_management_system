# library.py

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, year):
        self.books[isbn] = {'title': title, 'author': author, 'year': year, 'available': True}

    def get_book(self, isbn):
        return self.books.get(isbn)

    def borrow_book(self, isbn):
        book = self.get_book(isbn)
        if book and book['available']:
            book['available'] = False
        else:
            raise ValueError("Book not available")
    def return_book(self, isbn):
        book = self.get_book(isbn)
        if book:
            book['available'] = True
    
    def view_available_books(self):
        return {isbn: book for isbn, book in self.books.items() if book['available']}
    
    
    
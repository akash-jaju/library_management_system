
from library import Library  # This will be the main class where you implement your system

def test_add_book():
    library = Library()
    library.add_book('978-3-16-148410-0', 'Title', 'Author', 2021)
    assert library.get_book('978-3-16-148410-0') is not None


def test_borrow_book():
    library = Library()
    library.add_book('978-3-16-148410-0', 'Title', 'Author', 2021)
    library.borrow_book('978-3-16-148410-0')
    assert not library.get_book('978-3-16-148410-0')['available']


def test_return_book():
    library = Library()
    library.add_book('978-3-16-148410-0', 'Title', 'Author', 2021)
    library.borrow_book('978-3-16-148410-0')
    library.return_book('978-3-16-148410-0')
    assert library.get_book('978-3-16-148410-0')['available']


def test_view_available_books():
    library = Library()
    library.add_book('978-3-16-148410-0', 'Title', 'Author', 2021)
    assert '978-3-16-148410-0' in library.view_available_books()


from library import Library  # This will be the main class where you implement your system

def test_add_book():
    library = Library()
    library.add_book('978-3-16-148410-0', 'Title', 'Author', 2021)
    assert library.get_book('978-3-16-148410-0') is not None

class Book:
    def __init__(self, title, author):
        self.title = title                  # Public attribute
        self.author = author                # Public attribute
        self._is_checked_out = False        # Private attribute

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []   # private list of Book objects

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out the book with the given title, if available."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        # If no matching book found, do nothing silently (per instructions)

    def return_book(self, title):
        """Return the book with the given title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return

    def list_available_books(self):
        """Print available books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")


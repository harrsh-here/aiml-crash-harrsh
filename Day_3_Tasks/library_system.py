# Description: Implements a library catalog using class inheritance, method overriding, and polymorphism checks.

class LibraryItem:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def describe(self) -> str:
        return f"'{self.title}' by {self.author} ({self.year})"

class Book(LibraryItem):
    def __init__(self, title: str, author: str, year: int, pages: int):
        super().__init__(title, author, year)
        self.pages = pages

    def describe(self) -> str:
        return f"'{self.title}' by {self.author} ({self.year}) - {self.pages} pages"

class EBook(LibraryItem):
    def __init__(self, title: str, author: str, year: int, file_size_mb: float):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    def describe(self) -> str:
        return f"'{self.title}' by {self.author} ({self.year}) - {self.file_size_mb}MB"

if __name__ == "__main__":
    items = [
        Book("The Hobbit", "J.R.R. Tolkien", 1937, 310),
        Book("1984", "George Orwell", 1949, 328),
        EBook("Digital Renaissance", "John Doe", 2021, 4.5),
        EBook("Python Pro", "Jane Smith", 2023, 12.2)
    ]

    for item in items:
        print(item.describe())

    # calling isinstance(my_book, LibraryItem) returns True because Book is a subclass of LibraryItem,
    # meaning any instance of Book is structurally and behaviorally an instance of LibraryItem as well.
    print(isinstance(items[0], LibraryItem))
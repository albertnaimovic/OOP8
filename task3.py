# You need to create a program to manage a list of books in a library. Each book has a title, an author, a publication year, and an ISBN.
# You need to define a Book class using the dataclass module that contains attributes for these properties.
# You also need to implement a Library class that manages a list of books.
# The Library class should allow you to add and remove books from the library, search for books by title or author, and display the list of books currently in the library.

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Book:
    title: str
    author: str
    publication_year: int
    ISBN: str


class Library:
    BOOKS = []

    def add_book(self, book) -> None:
        self.BOOKS.append(book)

    def search_book(self, search_attribute: str) -> Optional["Book"]:
        for book in self.BOOKS:
            if search_attribute == book.title or search_attribute == book.author:
                return book
            return

    def display_books(self) -> str:
        print("Books in library:")
        for book in self.BOOKS:
            print(book)

    def remove_book(self, book_title: str) -> None:
        for book in self.BOOKS:
            if book_title == book.title:
                self.BOOKS.remove(book)


book_1 = Book(
    title="Don Quixote",
    author="Miguel de Cervantes",
    publication_year=2015,
    ISBN="515 51 65 18 ",
)

book_2 = Book(
    title="A Tale of Two Cities",
    author="Charles Dickens",
    publication_year=1869,
    ISBN="5342 421 61 18 ",
)

library = Library()

library.add_book(book_1)
library.add_book(book_2)

print(library.search_book("Don Quixote"))
library.display_books()

library.remove_book("Don Quixote")

library.display_books()

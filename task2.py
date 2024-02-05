# Create a set of data classes to model an online bookstore management system.
# The classes should include Author, Book, Customer, and Order.
# Your goal is to design a system that enables the management of books, authors, customers, and orders in an online bookstore.

# Author Class:
# Attributes: author_id (int), name (str), birth_year (int), books (List[Book]).
# Initialize the attributes in the init method.

# Book Class:
# Attributes: book_id (int), title (str), author (Author), publication_year (int), price (float), quantity_in_stock (int).
# Add a method sell that reduces the quantity_in_stock when a book is sold.

# Customer Class:
# Attributes: customer_id (int), name (str), email (str), orders (List[Order]).

# Order Class:
# Attributes: order_id (int), customer (Customer), books (List[Book]), total_price (float), status (str) - either "Pending" or "Shipped".
# Add a method calculate_total_price that calculates the total price of the order based on the books' prices and quantities.
# Add a method ship_order that changes the order status to "Shipped" and updates the stock quantity for each book.


from dataclasses import dataclass
from typing import List


@dataclass
class Author:
    author_id: int
    name: str
    birth_year: int
    books: List["Book"]

    def __init__(
        self, author_id: int, name: str, birth_year: int, books: List["Book"]
    ) -> None:
        self.author_id = author_id
        self.name = name
        self.birth_year = birth_year
        self.books = books


@dataclass
class Book:
    book_id: int
    title: str
    author: str
    publication_year: int
    price: float
    quantity_in_stock: int

    def sell(self) -> int:
        return self.quantity_in_stock - 1


@dataclass
class Customer:
    customer_id: int
    name: str
    email: str
    # orders: List["Order"]


@dataclass
class Order:
    order_id: int
    customer: Customer
    books: List["Book"]
    status: str = "Pending"

    def calculate_total_price(self) -> float:
        total_price = sum([Book.price for _ in self.books])
        return total_price

    def ship_order(self) -> str:
        self.status = "Shipped"
        for _ in self.books:
            Book.sell()
        return self.status


harry_potter_1 = Book(
    book_id=123,
    title="Harry Potter and the Sorcerer's Stone.",
    author="J.K. Rowling",
    publication_year=1997,
    price=50.0,
    quantity_in_stock=20,
)
harry_potter_2 = Book(
    book_id=124,
    title="Harry Potter and the Chamber of Secrets.",
    author="J.K. Rowling",
    publication_year=1998,
    price=39.0,
    quantity_in_stock=5,
)

rowling = Author(
    author_id=131,
    name="J.K. Rowling",
    birth_year=1950,
    books=[harry_potter_1, harry_potter_2],
)

print(rowling.books)

customer = Customer(customer_id=1356, name="Jonas", email="jonas69@one.lt")

order = Order(order_id=484, customer=customer, books=[harry_potter_1, harry_potter_2])

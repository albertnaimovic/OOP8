# Task Nr.1:

# You have been asked to create a simple inventory management system for a small retail store.
# You need to define a Product class using the dataclass module that represents a product in the store.
# Each Product should have an unique ID, a name, a description, a price, and a quantity in  stock.
# You also need to implement a method calculate_total_cost that calculates the total cost of a given number of items of the product,
# taking into account any discounts that may apply.

from dataclasses import dataclass


@dataclass
class Product:
    uniqueid: int
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def calculate_total_cost(self, discount: float = 100) -> float:
        return (self.price * self.quantity_in_stock) * (discount / 100)


phone = Product(
    uniqueid=1001,
    name="Iphone",
    description="Smartphone",
    price=1199.0,
    quantity_in_stock=10,
)

print(phone)
print(phone.calculate_total_cost(50))

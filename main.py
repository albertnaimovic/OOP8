from dataclasses import dataclass


@dataclass
class Address:
    street_name: str
    house_number: str
    postal_code: str


@dataclass
class Person:
    name: str
    age: int
    email: str
    address: Address

    def get_name(self) -> str:
        return self.name


person = Person(
    name="Albert",
    age=26,
    email="naimovic.albert@gmail.com",
    address=Address(street_name="Vilniaus", house_number="16", postal_code="13148"),
)



print(person.get_name())

# print(person, person.name, person.age, person.age == 26)

# person_one = Person(name="Albert", age=26, email="naimovic.albert@gmail.com")

# employee_list = [
#     person_one,
#     Person(name="Jonas", age=50, email="jonas.jonaitis@gmail.com"),
# ]


# class CEO:
#     apple = Person(name="Albert", age=26, email="naimovic.albert@gmail.com")
#     intel = Person(name="Andrius", age=46, email="andrius@gmail.com")


# print(CEO.apple.name)

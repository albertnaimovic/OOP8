# Create a flight ticketing mini system:

# The CLI should ask you to choose departure place and destination (minimum 5 cities) (Use dictionary to create a distance between the cities matrix map ).
# Then it should show options for at least 3 flight options with different different aircraft (Airbus A330-300, A340-300,A 340-600, A350- 100, Boeing 747-400, 747-800, 777-300).
# Every aircraft has different seat configuration (economy, business, first with different seat amount, seat pitch and average price)
# When you select the ticket (the provided option) the final cost should be calculated depending on aircraft type, departure time, and fuel consumption.
# (We can agree that flights that are departure earlier, has less seats and older, cost more). Use data classes and simple classes to achieve the result.

from dataclasses import dataclass
import os, time
from typing import List


@dataclass
class DistanceMap:
    distance_map: dict


@dataclass
class Aircraft:
    name: str
    economy_class_price: float
    business_class_price: float
    first_class_price: float
    seat_amount: int
    fuel_consumption_per_km: float


class Ticketeria:
    def __init__(self, distance_map: "DistanceMap") -> None:
        self.distance_map = distance_map

    def start(self) -> None:
        self.get_departure_city()

    def get_departure_city(self) -> None:
        distance_map = self.distance_map.distance_map
        while True:
            os.system("cls")
            counter = 1
            print("\n--Select departure city--\n")
            for x in distance_map:
                print(f"{counter}. {x}")
                counter += 1

            try:
                selection = int(input("\nSelect item: ")) - 1
                values_list = list(distance_map)
                departure_city = values_list[selection]

            except Exception:
                print(
                    "\nPlease enter number from list provided without any symbols and spaces."
                )
                time.sleep(2)
                continue
            break
        try:
            self.get_destination_city(distance_map, departure_city)
        except Exception as err:
            print(err)

    def get_destination_city(self, distance_map: dict, departure_city: str) -> None:
        while True:
            os.system("cls")
            counter = 1
            print("\n--Select destination city--\n")
            for x in distance_map[departure_city]:
                print(f"{counter}. {x}")
                counter += 1
            try:
                selection = int(input("\nSelect item: ")) - 1
                values_list = list(distance_map[departure_city])
                destination_city = values_list[selection]
                print(
                    f"Distance between {departure_city} and {destination_city} is {distance_map[departure_city][destination_city]} km"
                )
                input()
            except Exception:
                print(
                    "\nPlease enter number from list provided without any symbols and spaces."
                )
                time.sleep(2)
                continue
            break
        self.get_ticket_price(
            departure_city=departure_city,
            destination_city=destination_city,
            distance=distance_map[departure_city][destination_city],
        )

    def get_ticket_price(
        self, departure_city: str, destination_city: str, distance: float
    ) -> None:
        pass


distance_map = DistanceMap(
    {
        "Vilnius": {
            "Rome": 1702.0,
            "Berlin": 818.2,
            "Cape Town": 9886.5,
            "Sydney": 15283.3,
        },
        "Rome": {
            "Vilnius": 1702.0,
            "Berlin": 406.2,
            "Cape Town": 8686.5,
            "Sydney": 14283.3,
        },
        "Berlin": {
            "Vilnius": 818.2,
            "Rome": 406.2,
            "Cape Town": 8906.5,
            "Sydney": 14883.3,
        },
        "Cape Town": {
            "Vilnius": 9886.5,
            "Rome": 8686.5,
            "Berlin": 8906.5,
            "Sydney": 11013.1,
        },
        "Sydney": {
            "Vilnius": 15283.3,
            "Rome": 14283.3,
            "Berlin": 14883.3,
            "Cape Town": 11013.1,
        },
    }
)

aircraft_1 = Aircraft(
    name="Airbus A330-300",
    economy_class_price=50.0,
    business_class_price=100.0,
    first_class_price=150.0,
    seat_amount=100,
    fuel_consumption_per_km=10.0,
)
aircraft_2 = Aircraft(
    name="Boeing 747-400",
    economy_class_price=20.0,
    business_class_price=70.0,
    first_class_price=120.0,
    seat_amount=100,
    fuel_consumption_per_km=12.0,
)
aircraft_3 = Aircraft(
    name="Boeing 777-300",
    economy_class_price=30.0,
    business_class_price=80.0,
    first_class_price=140.0,
    seat_amount=100,
    fuel_consumption_per_km=15.0,
)


Ticketeria(distance_map).start()

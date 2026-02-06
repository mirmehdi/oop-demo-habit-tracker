# vehicle.py
# This file contains our "blueprints" (classes).
#
# Big OOP ideas we show here:
# 1) Class        -> blueprint (plan)
# 2) Object       -> real instance made from the blueprint
# 3) Attributes   -> data stored inside the object (e.g., seats)
# 4) Methods      -> functions inside the object (e.g., add passenger)
# 5) Inheritance  -> "is-a" relationship (Car IS A Vehicle)
# 6) Override     -> child class changes a parent method
# 7) super()      -> call the parent version of a method
# 8) Composition  -> "has-a" relationship (Convoy HAS vehicles)
# 9) Polymorphism -> different subclasses can be used in the same way

from __future__ import annotations # makes type hints “lazy” (not evaluated immediately).
from typing import List, Optional, Iterable # type-hint helpers. List = list type, Optional = value or None, Iterable = anything you can loop over.


class Vehicle:
    """
    Vehicle is the PARENT (base) class.
    A Vehicle has:
      - seats (capacity)
      - passengers (list of names)
    """

    def __init__(self, seats: int, passengers: Optional[Iterable[str]] = None) -> None:
        # __init__ is called automatically when you create an object.
        # This is the "constructor" in Python.
        #
        # Example:
        #   car = Vehicle(4)
        #
        # This will run __init__(seats=4)

        if not isinstance(seats, int) or seats <= 0:
            # We guard against bad inputs early.
            raise ValueError("seats must be a positive integer")

        self.seats = seats

        # We ALWAYS create a new list, so every Vehicle has its own passenger list.
        self.passengers: List[str] = list(passengers) if passengers is not None else []

    def __str__(self) -> str:
        # __str__ controls what you see when you do: print(vehicle)
        return f"Vehicle with {self.seats} seats and {len(self.passengers)} passenger(s)"

    def is_full(self) -> bool:
        # Method: returns True when vehicle reached capacity
        return len(self.passengers) >= self.seats

    def available_seats(self) -> int:
        # Method: how many empty seats are still available
        return self.seats - len(self.passengers)

    def add(self, name: str) -> None:
        """
        Add ONE passenger.
        - If the vehicle is full -> raise an error
        """
        name = name.strip()

        if not name:
            raise ValueError("name cannot be empty")

        if self.is_full():
            raise RuntimeError("Vehicle is full. No more seats.")

        self.passengers.append(name)

    def remove(self, name: str) -> bool:
        """
        Remove ONE passenger if present.
        Returns True if removed, False if not found.
        """
        try:
            self.passengers.remove(name)
            return True
        except ValueError:
            return False

    def print_passengers(self) -> None:
        # Nice printing for the passenger list
        if not self.passengers:
            print("  (no passengers)")
            return

        for i, p in enumerate(self.passengers, start=1):
            print(f"  {i}. {p}")

    def describe(self) -> str:
        """
        A method we will override (change) in child classes.
        This helps show inheritance + polymorphism.
        """
        return f"Vehicle(seats={self.seats}, passengers={len(self.passengers)})"


# ---------------------------
# INHERITANCE EXAMPLE #1
# ---------------------------
class Car(Vehicle):
    """
    Car is a CHILD class that inherits from Vehicle.
    Meaning: Car IS A Vehicle (inheritance: "is-a").

    Car also has extra attributes:
      - brand
      - model
    """

    def __init__(self, seats: int, brand: str, model: str, passengers: Optional[Iterable[str]] = None) -> None:
        # super() calls the parent (Vehicle) constructor,
        # so we do not rewrite the same code again.
        super().__init__(seats, passengers)

        self.brand = brand.strip()
        self.model = model.strip()

    def honk(self) -> None:
        # Extra method only for cars
        print("Beep beep!")

    # OVERRIDE: same method name, different behavior
    def describe(self) -> str:
        return f"Car({self.brand} {self.model}, seats={self.seats}, passengers={len(self.passengers)})"


# ---------------------------
# INHERITANCE EXAMPLE #2
# ---------------------------
class Bus(Vehicle):
    """
    Another child class.
    Bus IS A Vehicle.
    Buses often have a route number.
    """

    def __init__(self, seats: int, route_number: str, passengers: Optional[Iterable[str]] = None) -> None:
        super().__init__(seats, passengers)
        self.route_number = route_number.strip()

    def board_group(self, names: List[str]) -> None:
        """
        Add multiple passengers.
        We reuse Vehicle.add() to keep rules consistent.
        """
        for name in names:
            # This uses the parent method add()
            self.add(name)

    def describe(self) -> str:
        return f"Bus(route={self.route_number}, seats={self.seats}, passengers={len(self.passengers)})"


# ---------------------------
# COMPOSITION (HAS-A) EXAMPLE
# ---------------------------
class Convoy:
    """
    A Convoy is NOT a Vehicle.
    A Convoy HAS vehicles. (composition: "has-a")

    This is a great example to show:
    - how objects can contain other objects
    - how we can treat different vehicles the same way (polymorphism)
    """

    def __init__(self, name: str) -> None:
        self.name = name.strip()
        self.vehicles: List[Vehicle] = []   # Convoy stores Vehicle objects (or any subclass of Vehicle)

    def add_vehicle(self, vehicle: Vehicle) -> None:
        """
        Add a vehicle to the convoy.
        Note: It can be Vehicle, Car, Bus, etc. because Car/Bus are subclasses of Vehicle.
        """
        self.vehicles.append(vehicle)

    def total_seats(self) -> int:
        # Sum seats across all vehicles in the convoy
        return sum(v.seats for v in self.vehicles)

    def total_passengers(self) -> int:
        # Sum passengers across all vehicles in the convoy
        return sum(len(v.passengers) for v in self.vehicles)

    def print_summary(self) -> None:
        print(f"\nConvoy: {self.name}")
        print(f"Vehicles: {len(self.vehicles)}")
        print(f"Total seats: {self.total_seats()}")
        print(f"Total passengers: {self.total_passengers()}")

        # POLYMORPHISM:
        # We call v.describe() on each item.
        # Even though some are Car and some are Bus,
        # they all have a describe() method.
        print("\nVehicle details:")
        for v in self.vehicles:
            print(" -", v.describe())


# vehicle.py
# Simple OOP demo: class, object, attributes, methods,
# inheritance, override, super(), composition, polymorphism.


# =========================
# CLASS (Blueprint)
# =========================
class Vehicle:
    # Vehicle is a class (blueprint)
    # Objects (instances) will be created from this class

    def __init__(self, seats):
        # __init__ runs when you create an object
        # attributes = data stored in the object
        self.seats = seats
        self.passengers = []

    def add_passenger(self, name):
        """here we add passengers name"""
        # method = function inside the class (an action)
        if len(self.passengers) >= self.seats:
            print("Vehicle is full!")
            return
        self.passengers.append(name)

    def describe(self):
        # This method will be overridden in child classes
        return f"Vehicle: seats={self.seats}, passengers={len(self.passengers)}"


# =========================
# INHERITANCE (Car is-a Vehicle)
# =========================
class Car(Vehicle):
    # Car inherits from Vehicle
    # Meaning: Car IS A Vehicle

    def __init__(self, seats, brand):
        # super() calls the parent constructor (Vehicle.__init__)
        super().__init__(seats)
        self.brand = brand

    # OVERRIDE: same method name, different behavior
    def describe(self):
        return f"Car({self.brand}): seats={self.seats}, passengers={len(self.passengers)}"


# =========================
# INHERITANCE (Bus is-a Vehicle)
# =========================
class Bus(Vehicle):
    # Bus inherits from Vehicle

    def __init__(self, seats, route):
        super().__init__(seats)
        self.route = route

    # OVERRIDE
    def describe(self):
        return f"Bus(route {self.route}): seats={self.seats}, passengers={len(self.passengers)}"


# =========================
# COMPOSITION (Fleet has-a Vehicles)
# =========================
class Fleet:
    # Fleet is NOT a Vehicle.
    # Fleet HAS vehicles (composition).

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, v):
        # v can be Vehicle, Car, or Bus
        self.vehicles.append(v)

    def show_all(self):
        # POLYMORPHISM:
        # We call the same method (describe) on different object types.
        # Each object prints its own version (because of override).
        for v in self.vehicles:
            print(v.describe())

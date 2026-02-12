# vehicle.py
# OOP demo: class, object, attributes, methods,
# inheritance, override, super(), composition, polymorphism.

class Vehicle:
    """Vehicle: has seats and passengers, can add passengers."""

    def __init__(self, seats):
        self.seats = seats          # attribute
        self.passengers = []        # attribute

    def add_passenger(self, name):
        """Add a passenger if there is space."""
        if len(self.passengers) >= self.seats:
            print("Vehicle is full!")
            return
        self.passengers.append(name)

    def describe(self):
        """Return a short text about this object."""
        return f"Vehicle: seats={self.seats}, passengers={len(self.passengers)}"


class Car(Vehicle):
    """Car is a Vehicle (inheritance)."""

    def __init__(self, seats, brand):
        super().__init__(seats)     # super(): call parent constructor
        self.brand = brand

    def describe(self):
        """Override: same method name, different output."""
        return f"Car({self.brand}): seats={self.seats}, passengers={len(self.passengers)}"


class Bus(Vehicle):
    """Bus is a Vehicle (inheritance)."""

    def __init__(self, seats, route):
        super().__init__(seats)
        self.route = route

    def describe(self):
        return f"Bus(route {self.route}): seats={self.seats}, passengers={len(self.passengers)}"


class Fleet:
    """Fleet has vehicles (composition)."""

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, v):
        self.vehicles.append(v)

    def show_all(self):
        """Polymorphism: call describe() on different vehicle types."""
        for v in self.vehicles:
            print(v.describe())

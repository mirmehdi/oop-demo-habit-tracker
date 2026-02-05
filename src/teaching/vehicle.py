# vehicle.py
# OOP demo: class, object, attributes, methods (+ extra hooks for later)

from __future__ import annotations
from typing import List, Optional, Iterable


class Vehicle:
    """
    Vehicle = PARENT (base) class.

    Attributes (data):
      - seats: capacity
      - passengers: list of names

    Methods (actions):
      - add_passenger(name)
      - remove(name)
      - describe()
    """

    def __init__(self, seats: int, passengers: Optional[Iterable[str]] = None) -> None:
        if not isinstance(seats, int) or seats <= 0:
            raise ValueError("seats must be a positive integer")

        self.seats = seats
        self.passengers: List[str] = list(passengers) if passengers is not None else []

    def is_full(self) -> bool:
        return len(self.passengers) >= self.seats

    def add_passenger(self, name: str) -> None:
        """Add ONE passenger if there is space."""
        name = name.strip()
        if not name:
            raise ValueError("name cannot be empty")

        if self.is_full():
            raise RuntimeError("Vehicle is full. No more seats.")

        self.passengers.append(name)

    # short alias (optional)
    def add(self, name: str) -> None:
        """Alias for add_passenger(name)."""
        self.add_passenger(name)

    def remove(self, name: str) -> bool:
        """Remove passenger; return True if removed, False if not found."""
        try:
            self.passengers.remove(name)
            return True
        except ValueError:
            return False

    def print_passengers(self) -> None:
        if not self.passengers:
            print("(no passengers)")
            return
        for i, p in enumerate(self.passengers, start=1):
            print(f"{i}. {p}")

    def describe(self) -> str:
        return f"Vehicle(seats={self.seats}, passengers={len(self.passengers)})"

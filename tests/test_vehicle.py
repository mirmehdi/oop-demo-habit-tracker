# tests/test_vehicle.py
# Simple pytest tests for teaching OOP.
# Pattern: Arrange -> Act -> Assert

from src.teaching.vehicle import Vehicle


def test_vehicle_starts_empty():
    # Arrange
    v = Vehicle(2)

    # Act (nothing to do)

    # Assert
    assert v.seats == 2
    assert v.passengers == []


def test_add_passenger_adds_name():
    # Arrange
    v = Vehicle(2)

    # Act
    v.add_passenger("Alice")

    # Assert
    assert v.passengers == ["Alice"]


def test_vehicle_full_prints_message_and_does_not_add(capsys):
    # Arrange
    v = Vehicle(1)
    v.add_passenger("Alice")

    # Act
    v.add_passenger("Bob")  # should print "Vehicle is full!"

    # Assert (state)
    assert v.passengers == ["Alice"]

    # Assert (output)
    out = capsys.readouterr().out
    assert "Vehicle is full!" in out


# run PYTHONPATH=. ./env_habit/bin/python -m pytest -q

from src.teaching.vehicle import Vehicle, Car, Bus, Fleet


def test_inheritance_car_is_vehicle():
    c = Car(4, "Toyota")
    assert isinstance(c, Vehicle)


def test_override_describe_differs_by_type():
    v = Vehicle(2)
    c = Car(2, "Toyota")
    b = Bus(2, "M29")

    assert v.describe().startswith("Vehicle")
    assert c.describe().startswith("Car")
    assert b.describe().startswith("Bus")


def test_polymorphism_fleet_show_all(capsys):
    fleet = Fleet()
    fleet.add_vehicle(Vehicle(2))
    fleet.add_vehicle(Car(4, "Toyota"))
    fleet.add_vehicle(Bus(5, "M29"))

    fleet.show_all()

    lines = capsys.readouterr().out.strip().splitlines()
    assert len(lines) == 3
    assert lines[0].startswith("Vehicle")
    assert lines[1].startswith("Car")
    assert lines[2].startswith("Bus")

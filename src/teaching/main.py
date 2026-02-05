# main.py
# Run one small demo: class -> object, attributes, methods.

from vehicle import Vehicle


def demo_basics():
    """
    DEMO: Basics
    - Vehicle is a class (blueprint)
    - v1 is an object (instance)
    - seats/passengers are attributes
    - add_passenger/describe are methods
    """
    v1 = Vehicle(2)          # create object
    print(v1.seats)          # attribute

    v1.add_passenger("Alice")  # method
    v1.add_passenger("Bob")    # method

    print(v1.describe())       # method returning string
    v1.print_passengers()      # method printing list


if __name__ == "__main__":
    demo_basics()

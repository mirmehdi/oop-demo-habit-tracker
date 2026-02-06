import sys
from vehicle import Vehicle, Car, Bus, Fleet

# Each demo_* function focuses on ONE topic:
# - demo_basics()       -> class, object, attributes, methods
# - demo_inheritance()  -> inheritance, override, super()
# - demo_fleet()        -> composition + polymorphism

## for help: 
# python3 -c "from vehicle import Vehicle; help(Vehicle)"
# python3 main.py --help
# python3 main.py inheritance# 
# python3 -c "from vehicle import Vehicle; help(Vehicle.add_passenger)"

def demo_basics():
    """
    DEMO 1: Basics (class, object, attributes, methods)

    - Vehicle is a CLASS (blueprint).
    - v1 is an OBJECT (instance) created from the class.
    - v1.seats is an ATTRIBUTE (data in the object).
    - v1.add_passenger(...) is a METHOD (action in the object).
    """
    v1 = Vehicle(2)
    print(v1.seats)
    v1.add_passenger("Alice")
    v1.add_passenger("Bob")
    print(v1.describe())

def demo_inheritance():
    """
    DEMO 2: Inheritance + super() + override

    - Car and Bus are CHILD classes (subclasses) of Vehicle.
      Meaning: Car IS A Vehicle, Bus IS A Vehicle.
    - super().__init__(...) in Car/Bus calls the parent constructor in Vehicle.
      This avoids repeating the same setup code.
    - describe() is OVERRIDDEN in Car/Bus:
      same method name, but different output depending on object type.
    """
    c1 = Car(4, "Toyota")
    b1 = Bus(5, "M29")
    c1.add_passenger("Mehdi")
    b1.add_passenger("Dimitri")
    print(c1.describe())
    print(b1.describe())

def demo_fleet():
    """
    DEMO 3: Composition + Polymorphism

    - Fleet is NOT a Vehicle.
    - Fleet HAS vehicles (composition): it stores Vehicle objects inside it.
    - Polymorphism: we call v.describe() for each vehicle in the fleet,
      and it works for Vehicle, Car, and Bus even though they are different types.
      The result depends on the real object type (because of override).
    """
    v1 = Vehicle(2)
    c1 = Car(4, "Toyota")
    b1 = Bus(5, "M29")
    fleet = Fleet()
    fleet.add_vehicle(v1)
    fleet.add_vehicle(c1)
    fleet.add_vehicle(b1)
    print("Fleet summary:")
    fleet.show_all()

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "basics"

    if mode == "basics":
        demo_basics()
    elif mode == "inheritance":
        demo_inheritance()
    elif mode == "fleet":
        demo_fleet()
    else:
        print("Unknown mode. Use: basics | inheritance | fleet")

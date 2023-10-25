"""
The inheritance in object-oriented programming (OOP) is a mechanism 
that allows creating new classes from existing ones. In other words, 
a child class inherits the attributes and methods of its parent class. 
This means that the child class can use the same attributes and methods
 as its parent class, as well as add new attributes and methods of its own.
"""

class Vehicle:
    # attributes
    def __init__(self, brand, model, speed, year):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.year = year

    # methods
    def moreSpeed(self, speed):
        self.speed += speed

    def leesSpeed(self, speed):
        self.speed -= speed

class Motorcycle(Vehicle):
    def __init__(self, brand, model, speed, year, engiene):
        super().__init__(brand, model, speed, year)
        self.engiene = engiene

    def wheeliee(self):
        return "Doing wheelie..."

class Bus(Vehicle):
    def __init__(self, brand, model, speed, year, seats):
        super().__init__(brand, model, speed, year)
        self.seats = seats

    def getonPassengers(self, passengers):
        return f"passengers on board {passengers}"


moto = Motorcycle("Harley Davidson", 2023, 100, 2023, 1200)
print(moto.brand)
print(moto.wheeliee())

print()

bus = Bus("Vw", "Bus One", "100", "2020", "50" )
print(bus.brand)
print(bus.getonPassengers(bus.seats))

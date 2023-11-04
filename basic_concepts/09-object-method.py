"""
an object method is a function that is associated 
with an object. It is defined within a class and 
can be called on an instance of that class. Object 
methods are used to perform operations on the data 
that is stored within an object.
"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def increaseSpeed(speed):
        # self.speed += speed
        print(speed)

    def decreaseSpeed(self, speed):
        self.speed -= speed
        print(self.speed)


vehicle1 = Vehicle("Ford", 2020)

# vehicle1.decreaseSpeed(-20)
# vehicle1.increaseSpeed(20) #  NO!

# Vehicle.increaseSpeed(20)
# Vehicle.decreaseSpeed(25)

print(vehicle1.decreaseSpeed)
print(Vehicle.decreaseSpeed)

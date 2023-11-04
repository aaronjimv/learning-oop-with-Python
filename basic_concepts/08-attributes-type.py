# class attributes: are generally shared across all instances of the class.

# instance attributes: are different for each instance that assigns them values.

# data attributes: are unique to the instance in which it is created and initialized.

class Vehicle:
    # class attributes
    wheels = 4
    
    # instance attributes
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    # methods
    def increaseSpeed(self, speed):
        self.speed += speed

    def decreaseSpeed(self, speed):
        self.speed -= speed


# instance attributes
vehicle1 = Vehicle("Ford", 2022, 20)
print("instance 1")
print(vehicle1.wheels)

print()

vehicle1.wheels = 6  # create a unique copy of "wheels" in this instance

# class attributes

Vehicle.wheels = 6  # changes the value of "wheels" for all instances

vehicle2 = Vehicle("Mazda", 2020, 40)
print("instance 2")
print(vehicle2.wheels)
print(vehicle1.wheels)

# data attribute
vehicle2.color = "black"
print("Vehicle 2 - color")
print(vehicle2.wheels)

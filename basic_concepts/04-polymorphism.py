"""
Polymorphism  is a concept that describes the 
ability of an object to take on many forms. 
In other words, it allows objects of different 
types to be accessed through the same interface. 
Each type can provide its own independent implementation 
of this interface.
"""

class Shape:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius * 2, radius * 2)
        self.radius = radius

    def draw(self):
        print(
            f"Printing the shape of a circle {self.x}, {self.y} and its radius is {self.radius}"
        )


class Triangle(Shape):
    def __init__(self, x, y, base, height):
        super().__init__(x, y, height, base)
        self.base = base
        self.height = height

    def draw(self):
        print(
            f"Printing a triangle in {self.x}, {self.y} with a base {self.base} and a height {self.height}"
        )


class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)

    def draw(self):
        print(
           f"Printing a rectangle with its measurements {self.x}, {self.y} and with its width of {self.width}, and height of {self.height}"
        )


cir = Circle(x=50, y=50, radius=25)
tri = Triangle(x=100, y=100, base=50, height=150)
rec = Rectangle(x=300, y=200, height=100, width=200)

cir.draw()
tri.draw()
rec.draw()

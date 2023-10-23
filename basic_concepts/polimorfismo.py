class Shape:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw(self):
        pass


class Circulo(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius * 2, radius * 2)
        self.radius = radius

    def draw(self):
        print(
            f"Imprimiendo la forma de un circulo {self.x}, {self.y} y su radio es {self.radius}"
        )


class Tringulo(Shape):
    def __init__(self, x, y, base, height):
        super().__init__(x, y, height, base)
        self.base = base
        self.height = height

    def draw(self):
        print(
            f"Impriendo un triangulo en {self.x}, {self.y} con una base {self.base} y una altura {self.height}"
        )


class Rectangulo(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)

    def draw(self):
        print(
            f"Imprimiendo un rectangulo con sus medidas {self.x}, {self.y} y con su ancho de {self.width}, y altura de {self.height}"
        )


circulo = Circulo(x=50, y=50, radius=25)
tringulo = Tringulo(x=100, y=100, base=50, height=150)
rectangulo = Rectangulo(x=300, y=200, width=200, height=100)

circulo.draw()
tringulo.draw()
rectangulo.draw()

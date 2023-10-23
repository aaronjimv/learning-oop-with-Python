class MiClase:
    atributo_de_clase = 7

    def __init__(self, color):
        self.color = color
    
    @staticmethod
    def metodo_estatico(color):
        print(f"Este es un método estático del color {color}")
    
    @classmethod
    def metodo_de_clase(cls):
        print(cls.__name__)
        # print("Este es un método de clase con el atributo de clase", cls.atributo_de_clase)

miclase = MiClase("Yellow")
MiClase.metodo_estatico("Yellow")
MiClase.metodo_de_clase()
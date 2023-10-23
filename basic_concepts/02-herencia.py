class Vehiculo:
    # atributos
    def __init__(self, marca, modelo, velocidad, anio):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.anio = anio

    # métodos
    def darVelocidad(self, velocidad):
        self.velocidad += velocidad

    def reducirVelocidad(self, velocidad):
        self.velocidad -= velocidad


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad, anio, motor):
        super().__init__(marca, modelo, velocidad, anio)
        self.motor = motor

    # hacer caballito
    def Wheelie(self):
        return "Haciendo el wheelie..."


class Autobus(Vehiculo):
    def __init__(self, marca, modelo, velocidad, anio, asientos):
        super().__init__(marca, modelo, velocidad, anio)
        self.asientos = asientos

    def cargarPasajeros(self, pasajeros):
        return f"pasajero a bordo {pasajeros}"


motocicleta = Motocicleta("Honda", 2022, 100, 2023, 1200)
# print(motocicleta.marca)
# print(motocicleta.Wheelie())
autobus = Autobus(
    marca="Blubird", modelo=2010, velocidad=100, anio=2000, asientos=30
)
print(autobus.marca)
print(autobus.cargarPasajeros(60))

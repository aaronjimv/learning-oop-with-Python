class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def darVelocidad(velocidad):
        # self.velocidad += velocidad
        print(velocidad)

    def reducirVelocidad(self, velocidad):
        self.velocidad -= velocidad
        print(self.velocidad)


vehiculo1 = Vehiculo("Ford", 2020)

# vehiculo1.reducirVelocidad(-20)
# vehiculo1.darVelocidad(20) #  NO!
# Vehiculo.darVelocidad(20)
# Vehiculo.reducirVelocidad(25)

print(vehiculo1.reducirVelocidad)
print(Vehiculo.reducirVelocidad)

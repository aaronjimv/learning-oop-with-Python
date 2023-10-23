# atributos de clase: son compartidos de forma general para todas las instancias de la clase.
# atributos de instancia: son diferentes para cada una de las instancias que le asigna valores.
# atributos de datos: son únicos para la instancia en la que se crea y se inicializa.
class Vehiculo:
    # atributos de clase
    ruedas = 4
    
    # atributos de instancia
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    # métodos
    def darVelocidad(self, velocidad):
        self.velocidad += velocidad

    def reducirVelocidad(self, velocidad):
        self.velocidad -= velocidad


# atributos de instancia
vehiculo1 = Vehiculo("Ford", 2022, 20)
print("instancia 1")
print(vehiculo1.ruedas)

print()

vehiculo1.ruedas = 6  # crear una copia de "ruedas" única en esta instancia
# atributos de clase
Vehiculo.ruedas = 6  # cambia el valor de "ruedas" para todas las instancias

vehiculo2 = Vehiculo("Mazda", 2020, 40)
print("instancia 2")
print(vehiculo2.ruedas)
print(vehiculo1.ruedas)

# atributo de datos
vehiculo2.color = "black"
print("Vehiculo 2 - color")
print(vehiculo2.ruedas)

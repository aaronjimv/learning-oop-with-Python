class Usuario:
    def __init__(self, nombre, apellido, contrasenia):
        # atributos publicos
        self._nombre = nombre
        self._apellido = apellido
        self._contrasenia = self.encriptarContrasenia(contrasenia)

    def encriptarContrasenia(self, contrasenia):
        pass

    def verificarContrasenia(self, contrasenia):
        pass

    # getter
    @property
    def nombre(self):
        return self._nombre
    
    # setter
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # getter
    @property
    def apellido(self):
        return self._apellido
    
    # setter
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido


# instancia
usuario1 = Usuario("Echiro", "Oda", "test")
print(usuario1.nombre)
print(usuario1.apellido)

print("---")

usuario1.nombre = "Hiro"
usuario1.apellido = "Mashima"
print(usuario1.nombre)
print(usuario1.apellido)
class Usuario:
    def __init__(self, nombre, apellido, contrasenia, correo, telefono):
        # atributos publicos
        self.nombre = nombre
        self.apellido = apellido
        self.contrasenia = self.encriptarContrasenia(contrasenia)
        self.correo = correo
        # atributos privados
        self.__telefono = telefono

    def obtener_telefono(self):
        return self.__telefono

    def actualizar_telefono(self, nuevo_telefono):
        self.__telefono = nuevo_telefono

    def encriptarContrasenia(self, contrasenia):
        pass

    def verificarContrasenia(self, contrasenia):
        pass


usuario1 = Usuario(
    nombre="Mark",
    apellido="Zokenber",
    correo="mzok@gmail.com",
    contrasenia="test",
    telefono="1234",
)

usuario1.actualizar_telefono(5678)
print(usuario1.obtener_telefono())

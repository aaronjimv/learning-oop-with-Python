# ejemplo de clases
class Ususario():
    def __init__(self, nombre, apellido, correo, password, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = password
        self.telefono = telefono

    def encriptarContrasena(self):
        pass

    def verificarContrasena(self):
        pass

usuario1 = Ususario(
    nombre="Bill", 
    apellido="Gates", 
    correo="bg@gmail.com", 
    password="123", 
    telefono="12345"
    )

print(usuario1.nombre)
print(usuario1.apellido)
from cryptocode import encrypt, decrypt
from abc import ABC, abstractmethod

class UsuarioBase(ABC):
    def __init__(self, nombre, apellido, correo, password, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = self.encriptarContrasena(password)
        self.telefono = telefono

    @abstractmethod
    def encriptarContrasena(self):
        pass

    @abstractmethod
    def verificarContrasena(self):
        pass

class UsuarioConcreto(UsuarioBase):
    def encriptarContrasena(self, password):
        return encrypt(password, "secret")
    
    def verificarContrasena(self, password):
        descencripted_password = decrypt(self.password, "secret")
        return descencripted_password == password
    

usuario1 = UsuarioConcreto(
    nombre="Bill", 
    apellido="Gates", 
    correo="bg@gmail.com", 
    password="123", 
    telefono="12345"
)

print(usuario1.password)
print(usuario1.verificarContrasena("123"))

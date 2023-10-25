from cryptocode import encrypt, decrypt
from abc import ABC, abstractmethod

class UserBase(ABC):
    def __init__(self, name, lastname, email, password, phone):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = self.encryptPassword(password)
        self.phone = phone

    @abstractmethod
    def encryptPassword(self):
        pass

    @abstractmethod
    def checkPassword(self):
        pass

class UserParticular(UserBase):
    def encryptPassword(self, password):
        return encrypt(password, "secret")
    
    def checkPassword(self, password):
        decrypted_password = decrypt(self.password, "secret")
        return decrypted_password == password
    

user1 = UserParticular(
    name="Bill", 
    lastname="Gates", 
    email="bg@gmail.com", 
    password="123", 
    phone="12345"
)

print(user1.password)
print(user1.checkPassword("123"))
print(user1.checkPassword("abc"))
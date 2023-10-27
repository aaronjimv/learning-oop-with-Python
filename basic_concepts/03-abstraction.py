"""
The abstraction allows us to create a simplified version 
of an object that contains only the information necessary 
for our program. This simplified version is called an abstract 
class. An abstract class is like a template that defines the 
common characteristics of a group of objects.
"""

"""
In order to create abstract classes in Python, it is necessary to 
import the ABC class and the abstractmethod decorator from the abc 
(Abstract Base Classes) module. A module that is found in the 
language's standard library, so it is not necessary to install.
"""

from cryptocode import encrypt, decrypt
from abc import ABC, abstractmethod

# abstract class
class BaseClass(ABC):
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

class User(BaseClass):
    def encryptPassword(self, password):
        return encrypt(password, "secret")
    
    def checkPassword(self, password):
        decrypted_password = decrypt(self.password, "secret")
        return decrypted_password == password
    

user1 = User(
    name="Bill", 
    lastname="Gates", 
    email="bg@gmail.com", 
    password="123", 
    phone="12345"
)

print(user1.password)
print(user1.checkPassword("123"))
print(user1.checkPassword("abc"))
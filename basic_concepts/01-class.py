"""
A class in object-oriented programming (OOP) is like a mold for 
creating objects. That is, a class is a template that defines how 
certain types of objects are constructed. Every time an object is 
built from a class, what is called an instance of that class is created.
"""

# this is a class
class User():
    def __init__(self, name, lastname, email, password, phone):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.phone = phone

    def encryptPassword(self):
        pass

    def checkPassword(self):
        pass

# this is a instance
user1 = User(
    name="Bill", 
    lastname="Gates", 
    email="bg@gmail.com", 
    password="123", 
    phone="12345"
    )

print(user1.name)
print(user1.lastname)
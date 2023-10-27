"""
In object-oriented programming (OOP), getters and setters 
are methods that allow you to access and modify the values 
of private attributes in a class. Private attributes are those 
that are not meant to be accessed or modified directly from outside the class.
"""

"""
A getter is a method that returns the value of a private attribute. 
It allows you to access the value of the attribute without exposing it directly. 

A setter is a method that sets the value of a private attribute. 
It allows you to modify the value of the attribute without exposing it directly.
"""

"""
@property is a decorator, indicating that the next method is a 
property of the class. A property is a method that can be accessed 
as if it were an attribute, that is, without using parentheses. 
Properties serve to control access to the private attributes of 
the class, allowing them to be read or modified as desired.
"""

"""
Another decorator used is @name.setter and @lastname.setter, which 
indicates that the next method is a setter of the name and lastname property. 
"""

class User:
    def __init__(self, name, lastname, password):
        # Private attributes
        self.__name = name
        self.__lastname = lastname
        # Public attributes
        self.password = self.encryptPassword(password)

    def encryptPassword(self, password):
        pass

    def checkPassword(self, password):
        pass

    # getter
    @property
    def name(self):
        return self.__name
    
    # setter
    @name.setter
    def name(self, name):
        self.__name = name

    # getter
    @property
    def lastname(self):
        return self.__lastname
    
    # setter
    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname


user1 = User("Echiro", "Oda", "test")
print(user1.name)
print(user1.lastname)

print("---")

user1.name = "Hiro"
user1.lastname = "Mashima"
print(user1.name)
print(user1.lastname)
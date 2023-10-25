class User:
    def __init__(self, name, lastname, password):
        # atributos publicos
        self._name = name
        self._lastname = lastname
        self._password = self.encryptPassword(password)

    def encryptPassword(self, password):
        pass

    def checkPassword(self, password):
        pass

    # getter
    @property
    def name(self):
        return self._name
    
    # setter
    @name.setter
    def name(self, name):
        self._name = name

    # getter
    @property
    def lastname(self):
        return self._lastname
    
    # setter
    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname


# instancia
user1 = User("Echiro", "Oda", "test")
print(user1.name)
print(user1.name)

print("---")

user1.name = "Hiro"
user1.lastname = "Mashima"
print(user1.name)
print(user1.lastname)
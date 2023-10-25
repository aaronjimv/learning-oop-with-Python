# ejemplo de clases
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

user1 = User(
    name="Bill", 
    lastname="Gates", 
    email="bg@gmail.com", 
    password="123", 
    phone="12345"
    )

print(user1.name)
print(user1.lastname)
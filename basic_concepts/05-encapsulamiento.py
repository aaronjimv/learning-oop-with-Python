class User:
    def __init__(self, name, lastname, password, email, phone):
        # public attributes
        self.name = name
        self.lastname = lastname
        self.password = self.encryptPassword(password)
        self.email = email
        # private attributes
        self.__phone = phone

    def get_phone(self):
        return self.__phone

    def update_phone(self, new_phone):
        self.__phone = new_phone

    def encryptPassword(self, password):
        pass

    def checkPassword(self, password):
        pass


user1 = User(
    name="Mark",
    lastname="Zokenber",
    email="mzok@gmail.com",
    password="test",
    phone="1234",
)

user1.update_phone(5678)
print(user1.get_phone())

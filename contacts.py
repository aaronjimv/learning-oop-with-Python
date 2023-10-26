class BaseClass:
    contacts = [] # contacts list

    # save a contact in the list
    def add_contact(self, name, email, phone):
        user_data = {"name": name, "email": email, "phone": phone}
        self.contacts.append(user_data)

    def update_contact(self):
        pass

class Contacts(BaseClass):
    pass
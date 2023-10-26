class BaseClass:
    contacts = [] # contacts list

    # save a contact in the list
    def add_contact(self, name, email, phone):
        user_data = {"name": name, "email": email, "phone": phone}
        self.contacts.append(user_data)

    def update_contact(self):
        pass

    def search_contact(self):
        pass

    @classmethod
    def all_contacts(cls):
        return cls.contacts

class Contacts(BaseClass):
    def add(self, name, email, phone):
        self.add_contact(name, email, phone)

    def show_all_contacts(self):
        contacts = self.all_contacts()
        for contact in contacts:
            print(f"{contact['name'] - {contact['email']} - {contact['phone']}}")
    
    def search(self):
        pass

    def update(self):
        pass
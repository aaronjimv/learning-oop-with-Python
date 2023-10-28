from contacts import Contacts
from menu import MainMenu

if __name__ == '__main__':
    while True:
        option = MainMenu.showMainMenu()
        contacts = Contacts()

        match(option):
            case 1:  # add contact
                MainMenu.showMenuAddContact()
                name, email, phone = MainMenu.addConact()
                contacts.add(name, email, phone)
            case 2:  # contact list
                MainMenu.showMenuAllContact()
                contacts.show_all_contacts()
            case 3:  # search contacr
                MainMenu.showMenuSearchContact()
                email = MainMenu.searchContact()
                contact = contacts.search(email)
                if contact:
                    print(contact)
                else:
                    print("This contact does not exits.")
            case 4:  # update contact
                MainMenu.showMenuUpdate()
                MainMenu.showMenuAllContact()
                contacts.show_all_contacts()
                email = MainMenu.searchContact()
                contact = contacts.search(email)
                if contact:
                    name, phone = MainMenu.getConatactData()
                    response = contacts.update(contact["email"], name, phone)
                    print("This contact was updated succefully!")
            case 5:  # close app
                print("\nGood Bye!")
                break

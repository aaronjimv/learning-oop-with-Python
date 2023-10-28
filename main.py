from contacts import Contacts
from menu import MainMenu

if __name__ == '__main__':
    while True:
        option = MainMenu.show_main_menu()
        contacts = Contacts()

        match(option):
            case 1:  # add contact
                MainMenu.show_menu_add_contact()
                name, email, phone = MainMenu.add_conact()
                contacts.add(name, email, phone)
            case 2:  # contact list
                MainMenu.show_menu_all_contact()
                contacts.show_all_contacts()
            case 3:  # search contacr
                MainMenu.show_menu_search_contact()
                email = MainMenu.search_contact()
                contact = contacts.search(email)
                if contact:
                    print(contact)
                else:
                    print("This contact does not exits.")
            case 4:  # update contact
                MainMenu.show_menu_update()
                MainMenu.show_menu_all_contact()
                contacts.show_all_contacts()
                email = MainMenu.search_contact()
                contact = contacts.search(email)
                if contact:
                    name, phone = MainMenu.get_conatact_data()
                    response = contacts.update(contact["email"], name, phone)
                    print("This contact was updated succefully!")
            case 5:  # close app
                print("\nGood Bye!")
                break

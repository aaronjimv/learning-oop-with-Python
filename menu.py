class MainMenu():
    
    @staticmethod
    def show_main_menu():
        print()
        print("-------------------")
        print("  WORKS CONTACTS   ")
        print("-------------------")
        print("1. Add contact")
        print("2. Show all contacts")
        print("3. Search contact")
        print("4. Edit contact")
        print("5. Close app")
        print()
        
        option = int(input("Choose one option: "))
        while option > 5 or option < 1:
            print("Invalid option...")
            option = int(input("Choose one option: "))
        else:
            return option
        
    @staticmethod
    def show_menu_add_contact():
        print()
        print("-------------------")
        print("    ADD CONTACT   ")
        print("-------------------")
        print()

    @staticmethod
    def add_conact():
        name = input("Enter the name: ")
        email = input("Enter the email: ")
        phone = input("Enter the phone: ")
        return name, email, phone
    
    @staticmethod
    def show_menu_all_contact():
        print()
        print("-------------------")
        print("   CONTACTS LIST   ")
        print("-------------------")
        print("Name     | Email     | Phone     ")
        print()

    @staticmethod
    def show_menu_search_contact():
        print()
        print("-------------------")
        print("  SEARCH CONTACT  ")
        print("-------------------")
        print()
        
    @staticmethod
    def search_contact():
        return input("Enter the contact's email: ")

    @staticmethod
    def show_menu_update():
        print()
        print("-------------------")
        print("  UPDATE CONTACT  ")
        print("-------------------")
        print()

    @staticmethod
    def get_contact_email():
        return input("Enter the contact's email: ")
    
    @staticmethod
    def get_conatact_data():
        name = input("Enter the name: ")
        phone = input("Enter the phone: ")
        return name, phone
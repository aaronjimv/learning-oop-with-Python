class MainMenu():
    
    @staticmethod
    def showMainMenu():
        print("-------------------")
        print("  WORKS CONTACTS   ")
        print("-------------------")
        print("1. Add contact")
        print("2. Show all contacts")
        print("3. Search contact")
        print("4. Edit contact")
        print("5. Close app")
        
        option = int(input("Choose one option: "))
        while option > 5 or option < 1:
            print("Invalid option...")
            option = int(input("Choose one option: "))
        else:
            return option
        
    @staticmethod
    def showMenuAddContact():
        print("-------------------")
        print("    ADD CONTACT   ")
        print("-------------------")

    @staticmethod
    def addConact():
        name = input("Enter the name: ")
        email = input("Enter the email: ")
        phone = input("Enter the phone: ")
        return name, email, phone
    
    @staticmethod
    def showMenuAllContact():
        print("-------------------")
        print("   CONTACTS LIST   ")
        print("-------------------")
        print("Name     | Email     | Phone     ")

    @staticmethod
    def showMenuSearchContact():
        print("-------------------")
        print("  SEARCH CONTACT  ")
        print("-------------------")
        
    @staticmethod
    def searchContact():
        return input("Enter the contact's email: ")

    @staticmethod
    def showMenuUpdate():
        print("-------------------")
        print("  UPDATE CONTACT  ")
        print("-------------------")

    @staticmethod
    def getContactEmail():
        return input("Enter the contact's email: ")
    
    @staticmethod
    def getConatactData():
        name = input("Enter the name: ")
        phone = input("Enter the phone: ")
        return name, phone
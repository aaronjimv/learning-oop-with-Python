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
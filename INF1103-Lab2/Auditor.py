inventory = 0
option = 0
errmsg = []
errInv = []
crInv = []

errors = []
quit = False
msg = ""

def mainMenu():
    print("=============================")
    print("Welcome to the Inventory Management System: ")
    print("1. Add Inventory")
    print("2. Remove Inventory")
    print("3. Quit")
    print("=============================")



while quit == False:

    mainMenu()
    option = input("Select an option: ")

    if option.isdigit() == True:
        option = int(option)
        if option == 1:
            print()

        elif option == 2:
            print()

        elif option == 3:
            print("=============================")
            print(f"Thank you for using the system!")
            print("=============================")

            quit = True

    else:
        print("Sorry Invalid Option, Please Try Again...")
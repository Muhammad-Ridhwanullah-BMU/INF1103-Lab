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
                    if inventory < 500:
                        add = input("Number of inventory to add: ")
                        if add.isdigit() == True and int(add) > 0:
                            add = int(add)
                            if (inventory + add) <= 500:
                                inventory += add
                                crInv.append(add)
                                print(f"SUccessfully added {add} to the inventory !\nInventory total: {inventory}")     
        
                            else:
                                msg = "Inventory Overflow, operation cancelled !"
                                errInv.append(add)
                                errors.append(msg)
                                print(msg)
        
                        elif add.isdigit() == False:
                            msg = "Not a digit, operation cancelled !"
                            errInv.append(add)
                            errors.append(msg)
                            print(msg)
        
                        else:
                            msg = "Negative numbers not accepted, operation cancelled !"
                            errInv.append(add)
                            errors.append(msg)
                            print(msg)
        
                    else:
                        msg = "Inventory full, operation cancelled !"
                        print(msg)

        elif option == 2:
                    if inventory > 0:
                        sub = input("Number of inventory to remove: ")
                        if sub.isdigit() == True and int(sub) > 0:
                            sub = int(sub)
                            if sub > inventory:
                                errInv.append(sub)
                                errors.append("Not enough inventory to remove")
                                print("Not enough inventory to remove, operation cancelled !")
        
                            else:
                                inventory -= sub
                                crInv.append(sub)
                                print(f"Successfully removed {sub} from the inventory !\nInventory total: {inventory}")
        
                        elif sub.isdigit() == False:
                            msg = "Not a digit, operation cancelled !"
                            errInv.append(sub)
                            errors.append(msg)
                            print(msg)
        
                        else:
                            msg = "Negative numbers not accepted, operation cancelled !"
                            errInv.append(sub)
                            errors.append(msg)
                            print(msg)
        
                    else:
                        msg = "Inventory empty, operation cancelled !"
                        print(msg)

        elif option == 3:
                    print("=============================")
                    print(f"Thank you for using the system!")
                    print("=============================")
        
                    if len(errors) != 0 or len(crInv) != 0:
                        print("Total Inventory: ", inventory)
                        print("Successful Transactions: ", len(crInv))
                        for number, amount in enumerate(crInv, start=1):
                            print(f"S/N{number}\nAmount: ${amount}\n")
                        print("=============================")
                        print("Unsuccessful Transactions: ", len(errInv))
                        for number, (invalid_input, reason) in enumerate(zip(errInv, errors), start=1):
                            print(f"S/N{number}\nInput: {invalid_input}\nReason: {reason}")
                        print("=============================")

                    else:
                         print("No changes made !")
        
                    quit = True
        else:
                print("Sorry Invalid Option, Please Try Again...")

    else:
        print("Sorry Invalid Option, Please Try Again...")
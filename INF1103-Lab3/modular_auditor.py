inventory = 0
option = 0
errmsg = []
errInv = []
crInv = []

errors = []
quit = False
msg = ""
failed_attempts = 0
deliveries_processed = 0

def mainMenu():
    print("=============================")
    print("Welcome to the Inventory Management System: ")
    print("1. Add Inventory")
    print("2. Remove Inventory")
    print(f"Type{"quit"} to end program")
    print("=============================")

def get_valid_input():
    global failed_attempts

    value = input("Enter stock quantity: ")

    if value.lower() == "quit":
        return "quit"

    elif value.isdigit() == True and int(value) > 0:
        value = int(value)
        return value

    elif value.startswith("-") and value[1:].isdigit():
        msg = "Negative numbers not accepted, operation cancelled !"

        errInv.append(value)
        errors.append(msg)

        failed_attempts += 1

        print(msg)

        return None

    else:
        msg = "Not a digit, operation cancelled !"

        errInv.append(value)
        errors.append(msg)

        failed_attempts += 1

        print(msg)

        return None

def calculate_tax(amount):
    tax = amount * 0.10
    print(f"Tax amount for {amount} units is ${tax}")
    return tax

def process_delivery(current_total, new_value):
    current_total += new_value
    print("Delivery Processed !")
    print("Total Inventory: ", current_total)
    return current_total

def generate_report(deliveries_processed, failed_attempts):
    print("=============================")
    print("Thank you for using the system!")
    print("=============================")

    if len(crInv) != 0:
        print("Total Inventory: ", inventory)
        print("Total Transactions processed: ", deliveries_processed)
        print("Successful Transactions: ", len(crInv))
        for i in range(len(crInv)):
            print(f"S/N: {i+1}\nAmount: {crInv[i]}\n")

    if len(errors) != 0:
        print("=============================")
        print("Unsuccessful Transactions: ", len(errInv))
        for i in range(len(errInv)):
                print(f"S/N: {i+1}\nInput: {errInv[i]}\nReason: {errors[i]}")
        print("=============================")

    if len(errors) == 0 and len(crInv) == 0:
        print("No changes made !")
         
    
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
        
                        elif add.startswith("-") and add[1:].isdigit():
                            msg = "Negative numbers not accepted, operation cancelled !"
                            errInv.append(add)
                            errors.append(msg)
                            print(msg)
        
                        else:
                            msg = "Not a digit, operation cancelled !"
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
        
                        elif sub.startswith("-") and sub[1:].isdigit():
                            msg = "Negative numbers not accepted, operation cancelled !"
                            errInv.append(sub)
                            errors.append(msg)
                            print(msg)
        
                        else:
                            msg = "Not a digit, operation cancelled !"
                            errInv.append(sub)
                            errors.append(msg)
                            failed_attempts += 1
                            print(msg)
        
                    else:
                        msg = "Inventory empty, operation cancelled !"
                        print(msg)

        else:
            if "quit" in option.lower():
                quit = True
            else:
                print("Sorry Invalid Option, Please Try Again...")

    else:
        print("Sorry Invalid Option, Please Try Again...")






















































































while quit == False:

    mainMenu()
    option = input("Select an option: ")

    if get_valid_input(option) != "quit":
        option = int(option)
        if option == 1:
                    if inventory < 500:
                        add = input("Number of inventory to add: ")
                        if get_valid_input(add) != "quit":
                            if (inventory + add) <= 500:
                                process_delivery(add)
                                calculate_tax(add)
                                crInv.append(add)   
        
                            else:
                                msg = "Inventory Overflow, operation cancelled !"
                                errInv.append(add)
                                errors.append(msg)
                                print(msg)
        
                        else:
                            if add.startswith("-") and add[1:].isdigit():
                                msg = "Negative numbers not accepted, operation cancelled !"
                                errInv.append(add)
                                errors.append(msg)
                                print(msg)
                            else:
                                msg = "Not a digit, operation cancelled !"
                                errInv.append(add)
                                errors.append(msg)
                                print(msg)
        
                    else:
                        msg = "Inventory full, operation cancelled !"
                        print(msg)

        elif option == 2:
                    if inventory > 0:
                        sub = input("Number of inventory to remove: ")
                        if get_valid_input(sub) != "quit":
                            sub = int(sub)
                            if sub > inventory:
                                errInv.append(sub)
                                errors.append("Not enough inventory to remove")
                                print("Not enough inventory to remove, operation cancelled !")
        
                            else:
                                process_delivery(-sub)
                                crInv.append(sub)
                                print(f"Successfully removed {sub} from the inventory !\nInventory total: {inventory}")
        
                        else:
                            if sub.startswith("-") and sub[1:].isdigit():
                                msg = "Negative numbers not accepted, operation cancelled !"
                                errInv.append(sub)
                                errors.append(msg)
                                print(msg)
        
                            else:
                                msg = "Not a digit, operation cancelled !"
                                errInv.append(sub)
                                errors.append(msg)
                                print(msg)
        
                    else:
                        msg = "Inventory empty, operation cancelled !"
                        print(msg)

        elif option == 3:

            if len(errors) and len(crInv) == 0:
                print("No changes made !")
            else:
                generate_report(inventory, errInv)

            quit = True

        else:
            print("Sorry Invalid Option, Please Try Again...")

    else:
        print("Sorry Invalid Option, Please Try Again...")
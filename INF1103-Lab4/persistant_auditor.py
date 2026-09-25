inventory = 0
inventoryList = []
option = 0
quit = False
errInv = []
taxes = []
crInv = []
errors = []
msg = ""
filePath = r"C:\INF1103-Labs\INF1103-Lab4\Orders.txt"
failed_attempts = 0
deliveries_processed = 0

def mainMenu():
    print("=============================")
    print("Welcome to the Inventory Management System")
    print("- Add to Inventory -")
    print("=============================")

def get_valid_input():
    global failed_attempts
    value = input("Enter stock quantity (Type [quit] to end program): ")
    print("=============================================================")

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
    print("=============================")
    print("Delivery Processed !")
    print("Total Inventory: ", current_total)
    print("=============================")
    return current_total

def generate_report(deliveries_processed, failed_attempts):
    print("=============================")
    print("Thank you for using the system!")
    print("=============================")

    if len(crInv) != 0:
        print("Total Inventory: ", inventory)
        print("Total Units Processed: ", deliveries_processed)
        print("Successful Transactions: ", len(crInv))
        for i in range(len(crInv)):
            print(f"ID: {inventoryList[i][0]}\nProduct Name: {inventoryList[i][1]}\nAmount: {inventoryList[i][2]}\n")
            print(f"Taxes: ${taxes[i]}\n")

    if len(errors) != 0:
        print("=============================")
        print("Unsuccessful Transactions: ", len(errInv))
        for i in range(len(errInv)):
                print(f"S/N: {i+1}\nInput: {errInv[i]}\nReason: {errors[i]}")
        print("=============================")

    if len(errors) == 0 and len(crInv) == 0:
        print("No changes made !")

def load_inventory():
    global inventory
    global inventoryList

    with open(filePath, "a+") as file:
        file.seek(0)

        for line in file:
            line = line.strip()

            if line != "":
                print("Current Orders:")
                productID, product, quantity = line.split(",")

                quantity = int(quantity)

                inventoryList.append(
                    (productID, product, quantity)
                )

                inventory += quantity

                print(f"ID: {productID}")
                print(f"Product: {product}")
                print(f"Quantity: {quantity}")
                print("=============================")

def save_inventory(item):
    with open(filePath, "a") as file:
        file.write(f"{item[0]},{item[1]},{item[2]}\n")
        print(f"New Order Added: \n{item[0]}, {item[1]}, {item[2]}\n\nOrder Successfully saved in Orders.txt !")

mainMenu()
load_inventory()

while quit == False:

    if inventory < 500:
        add = get_valid_input()

        if add == "quit":
            generate_report(inventory,failed_attempts)
            quit = True

        elif add != None:
            if (inventory + add) <= 500:
                tax = calculate_tax(add)
                taxes.append(tax)
                inventory = process_delivery(inventory,add)
                crInv.append(add)
                deliveries_processed += 1

            else:
                msg = ("Inventory Overflow, operation cancelled !")
                errInv.append(add)
                errors.append(msg)
                failed_attempts += 1
                print(msg)

    else:
        msg = ("Inventory full, operation cancelled !")
        print(msg)






















































































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
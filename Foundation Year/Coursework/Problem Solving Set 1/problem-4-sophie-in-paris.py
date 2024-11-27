# Problem 4 - Rodin Opuz
# This is the inventory I decided to create. It has 5 different items, with different quantities and different prices for each one.
# I decided on the specific items because I wanted them to be varied.
# This is a nested dictionary, it has the item's name then the quantity and price.
inventory = {"White Skirt": {"quantity": 10, "price": 19.99}, "Red Shirt": {"quantity": 27, "price": 14.99}, "Black Leggings": {"quantity": 5, "price": 9.99}, "Pink Socks": {"quantity": 9, "price": 4.00}, "Boutique Keychain": {"quantity": 2, "price": 1.99}}

# This is a while loop so the code runs indefinitely instead of only executing once.
while True:
    # This is the menu I created. There are 5 different options. It also has the title and an input which asks the user to enter an input between 1 - 5.
    print("""Sophie's Boutique - Inventory Management System
    1. Add Inventory Items
    2. Update Inventory Items
    3. Remove Items from Inventory
    4. Display Inventory
    5. Calculate Total Inventory Value""")
    menu_choice = input("Which option? Enter a number between 1 and 5 - ")
                                                                           


    # This is menu option 1. It is for adding items.
    if menu_choice == '1':
        item = input("Enter the name of the item: ").title().strip() # This capitalises the first character of each letter, all other letters being lowercase and removes any spaces to maintain consistency.
        # If the item is already in the inventory, it prevents it from being added again with an output explaining it.
        if item in inventory: 
            print(f"{item} is already in the management system. ")
        # If the item is not in the inventory it will ask for the quantity and price of the item.
        else:
            try: # This is to prevent any inputs from crashing the program.
                quantity = int(input(f"Enter the quantity of {item}. Enter a positive integer: ")) # It asks for an integer input.
                price = float(input(f"Enter the price of {item}. Enter a positive decimal number: ")) # It asks for a float input.
                # If the quantities are negative or zero, it will an output an error message.
                if quantity < 0 or price < 0:
                    print("You have not entered correct information. Please try again. ")
                # If the quantities are correct, it will add the item with its quantity and price to the dictionary. It also formats the price to 2 decimal places.
                else:
                    inventory[item] = {"quantity": quantity, "price": price}
                    print(f"Item: {item} - Quantity: {quantity} - Price: {price:.2f}. The item information has been added to the inventory system. ")
            # This will output if the input entered by the user would cause the program to crash. Exception handling.
            except:
                print("You have entered an invalid input. Please try again. ")



    # This is menu option 2. It is for updating items.
    elif menu_choice == "2":
        item = input("Enter the name of the item to update: ").title().strip() # The inputs are case and space insensitive. Example: "   whITE sKiRT  " --> "White Skirt". It asks for the item to be updated first.
        # If the item is not in the inventory dictionary, it outputs a message saying the item cannot be updated because it is not in the inventory dictionary.
        if item not in inventory:
            print(f"{item} is not in the management system. ")
        # If the item is in the inventory, it allows the user to either update the quanitity, price or both for the item.
        else:
            try: # Exception handling to prevent any inputs that are not an integer for quantity or not a float for price.
                update_choice = input(f"Do you want to update quantity, price or both for {item}: ").lower()
                
                # If the user inputs quantity then it will ask for a positive integer for the quantity
                if update_choice == "quantity":
                    quantity = int(input(f"Enter the new quantity of {item}. Enter a positive integer. "))
                    # If the quantity is 0 or negative, it will output an error message.
                    if quantity < 0:
                        print("You have not entered a positive integer. Please try again.")
                    # If the quantity value is correct, it will update the quantity and output a message confirming it. 
                    else:
                        inventory[item]["quantity"] = quantity
                        print(f"{item} has been updated with quantity {quantity}.")
                        
                # If the user inputs price then it will ask for a positive float for the price.
                elif update_choice == "price":
                    price = float(input(f"Enter the new price of {item}. Enter a positive decimal number. "))
                    # If the price is negative or 0, it will output an error message.
                    if price < 0:
                        print("You have not entered a positive decimal number. Please try again.")
                    # If the price is a positive decimal number, it will update the price for the item.
                    else:
                        inventory[item]["price"] = price
                        print(f"{item} has been updated with price {price:.2f}.")

                # If the user inputs both then it will ask for a quantity then an integer.
                elif update_choice == "both":
                    quantity = int(input(f"Enter the quantity of {item}. Enter a positive integer: "))
                    price = float(input(f"Enter the price of {item}. Enter a positive decimal number: "))
                    # If either of the values are negative or 0, it will output an error message.
                    if quantity < 0 or price < 0:
                        print("You have entered incorrect information. Please try again.")
                    # If both values are correct, it will update both values for the item.
                    else:
                        inventory[item] = {"quantity": quantity, "price": price}
                        print(f"Item: {item} - Quantity: {quantity} - Price: {price:.2f}. The item information has been updated. ")
                # If the user inputs a value that isnt quantity, price or both, it will output an error message.
                else:
                    print("You have not entered a valid option. Please try again.")
            # This will output if any input the user enters would crash the program.
            except:
                print("You have entered an invalid input. Please try again. ")                



    # This is menu option 3. It is for removing items.
    elif menu_choice == "3":
        item = input("Enter the name of the item to remove: ").title().strip() # To maintain consistency with item names and to prevent logic errors. Example: "white skirt" being different to "WHITE SKIRT  ".
        # If the item is not in the dictionary, it will output an error message.
        if item not in inventory:
            print(f"{item} is not in the inventory. ")
        # If the item is in the inventory it will remove the item using pop.
        else:
            inventory.pop(item)
            print(f"{item} has been removed from the inventory. ")


    # This is menu option 4. It is for viewing the inventory.
    elif menu_choice == "4":
        print("\nSophie's Boutique - Inventory")
        # This iterates through the different items in the inventory. It prints the item's name and then stores the key into info.
        for i in inventory:
            print(f"{i}")
            info = inventory[i]
            # This iterates through the item's prices and quantity.
            for j in info:
                # If the value is price it prints out the value. Example: Price - 19.99. It formats the price to two decimal places.
                if j == "price":
                    print(f"\t{j.capitalize()} - {info[j]:.2f}")
                # If the value is quantity it prints out the value. Example: Quantity - 5.
                else:
                    print(f"\t{j.capitalize()} - {info[j]}")
            print() # This is to make the program easier to read.


    # This is menu option 5. It is for calculating the total value of the inventory.
    elif menu_choice == "5":
        total_value = 0 # This creates the variable for the total value of the dictionary.
        # This iterates through the inventory and adds the quantity x price for each item.
        for i in inventory:
            total_value += inventory[i]["quantity"] * inventory[i]["price"]
        print(f"£{total_value:.2f} is the total inventory value.") # This prints out the total value and formats it to two decimal places.


    # This is when the user has not input a number between 1 and 5. 
    else:
        print("You have not entered a valid option. Please try again.")



    print() # To make it easier to read by spacing out the output.

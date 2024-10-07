while True:
    core = input("Enter core ingredient. Chicken or prawn? ")
    
    if core.lower() == "chicken":
        flavour = input("Enter preferred flavour. Indian or Thai? ")
        spice = input("Enter spice level. Mild or hot?")
        if flavour.lower() == "indian":
            if spice.lower() == "mild":
                print("Chicken Korma")
            elif spice.lower() == "hot":
                print("Chicken Tikka Masala")
            else:
                print("???")
        elif flavour.lower() == "thai":
            if spice.lower() == "mild":
                print("Thai Yellow Curry")
            elif spice.lower() == "hot":
                print("Thai Green Curry")
            else:
                print("???")
        else:
            print("???")
            
    elif core.lower() == "prawn":
        flavour = input("Enter preferred flavour. Thai or Malaysian? ")
        spice = input("Enter spice level. Mild or hot?")
        if flavour.lower() == "thai":
            if spice.lower() == "mild":
                print("Pad Thai")
            elif spice.lower() == "hot":
                print("Thai Red Curry")
            else:
                print("???")
        elif flavour.lower() == "malaysian":
            if spice.lower() == "mild":
                print("Fried Butter Prawn")
            elif spice.lower() == "hot":
                print("Prawn Laksa Curry Bowl")
            else:
                print("???")
        else:
            print("???")
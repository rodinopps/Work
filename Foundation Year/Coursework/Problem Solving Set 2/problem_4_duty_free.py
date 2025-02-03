# Problem 4 - Rodin Opuz
# Duty Free
# This outputs the best possible solution. The most chocolates and the least change possible.
five_thb = 3 * 5 # This is the total value of all the 5 THB notes we have. 
ten_thb = 4 * 10 # This is the total value of all the 10 THB notes we have. 
two_thb = 5 * 2 # This is the total value of all the 2 THB notes we have. 
twenty_thb = 3 * 20 # This is the total value of all the 20 THB notes we have. 
wallet = five_thb + ten_thb + two_thb + twenty_thb # This is the total amount of baht we have. 125

toblerone_price = 10 # This is how much a toblerone costs.
lindt_lindor_price = 5 # This is how much a lindt lindor costs.
kit_kat_price = 2 # This is how much a kit kat costs.

# This is a function that creates a solution for the problem. The best possible combination of chocolates.
def chocolate(wallet): # This is a function that takes wallet as a parameter.
    if wallet <= 3: # If the total amount of baht is less than 3, then it will run the code below.
        
        kit_kat = wallet // kit_kat_price # This calculates how many kit kats can be bought.
        wallet -= kit_kat * kit_kat_price # This subtracts the cost of the kit kats from the wallet.

        lindt_lindor = 0 # This calculates how many lindt lindors can be bought. (0) because it cannot be bought.

        toblerone = 0 # This calculates how many toblerone can be bought. (0) because it cannot be bought.
        
    else: # If the total amount of baht is greater than 3, it will run the code below.
        
        kit_kat = wallet // kit_kat_price # This calculates how many kit kats can be bought.
        wallet -= kit_kat * kit_kat_price # This subtracts the cost of the kit kats from the wallet.
        
        if wallet == 1: # If the wallet is 1 baht, it runs the code below.
            
            wallet += 4 # It reverses by adding 4 baht.
            kit_kat -= 2 # It reverses by subtracting 2 kit kats from the total bought. This is so a lindt lindor can be bought to ensure there is no change left.
        
            lindt_lindor = wallet // lindt_lindor_price # This calculates how many lindt lindors can be bought.
            wallet -= lindt_lindor * lindt_lindor_price # This subtracts the cost of the lindt lindors from the wallet.

            toblerone = wallet // toblerone_price # This calculates how many toblerone can be bought. (0)
            wallet -= toblerone * toblerone_price # This subtracts the cost of the toblerones from the wallet. (0)
        
        elif wallet == 0: # If the wallet value is 0 after buying kit kats, it runs this code instead below.
        
            lindt_lindor = 0 # This calculates how many lindt lindors can be bought. (0) because there is no change left.
        
            toblerone = 0 # This calculates how many toblerone can be bought. (0) because there is no change left.

    chocolate_total_amount = kit_kat + lindt_lindor + toblerone # After, it adds all the amounts of chocolates up together after buying them.

    if wallet != 0: # If there is change still left, it will store a message confirming this in the text variable.
        text = "There is no solution possible without change. " # This is the message confirming it.
    else: # If there is no change left, it will store a message that confirms that in the text variable.
        text = "This is the perfect solution. " # This is the message confirming it.
        
    return f"""
{text}
Toblerone - ({toblerone})
Lindt Lindor - ({lindt_lindor})
Kit Kat - ({kit_kat})

Chocolates - ({chocolate_total_amount})
Change - ({wallet})
    """
# This prints out the message which confirms whether or not there was change left, the amount of toblerones, lindt lindors and kit kats bought. The total amount of chocolate and the change left.

print(chocolate(wallet)) # This calls the function and passes the value in wallet as a parameter.

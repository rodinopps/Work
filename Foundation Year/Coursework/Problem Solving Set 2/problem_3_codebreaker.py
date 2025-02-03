# Problem 3 - Rodin Opuz
# Codebreaker



# This generates the list of prime numbers up to n.
def prime_number_list_generator(n): # This is a function that takes n as a parameter.
    prime_check, prime_list = [], [] # This creates two lists. prime_check will store boolean values that indicate if it is prime and prime_list to store the prime numbers.
    
    for i in range(n + 1): # This iterates n + 1 times. 
        prime_check.append(True) # This appends the value True to the list.
        
    p = 2 # This starts off with the smallest prime number which is 2.

    while p * p <= n: # This will keep iterating while p * p is lesser than or equal to n.
        if prime_check[p]: # This checks if prime_check[p] is True. If it is, it will run the code below.
            for i in range(p * p, n + 1, p): # This is a for loop that starts with the value p * p, ends at n + 1 and increases p times every step.
                prime_check[i] = False # This is for all multiples of 2. If it is a multiple of 2, the value at index i becomes False. This means it is not a prime number.
                
        p += 1 # This adds 1 to p which goes to the next number.
        
    for i in range(2, n + 1): # This is used to find the prime numbers. This starting value is 2 and ends at n + 1 for the for loop.
        if prime_check[i]: # If the value in the prime_check i index is True, it will append i to the prime_list.
            prime_list.append(i) # This appends i to the prime_list since it is prime which is indicated by the index i in prime_check being True.
    return prime_list # Once the for loop is done iterating, it returns the list prime_list.



# This uses the list of primes to factorise the number input by the user and store it in the list.
def prime_factorisation_of_a_number(n, prime_list): # This is a function that takes n and prime_list as parameters.
    prime_factors = [] # This is an empty list which will store the prime factors of the number n.
    
    for i in prime_list: # This iterates through the prime_list which consists of the prime numbers up to n.
        while n % i == 0: # While n is divisible by i, it will append i to the list factors.
            prime_factors.append(str(i)) # This converts i to a string data type. This is so it can output the list of factors using the join method.
            n /= i # Once i is appended to the list, it will divide n by i (the prime number) until it is not divisible.
        if n == 1: # Once n becomes 1 which means it is fully factorised, it exits.
            break # This exits the loop.
    return prime_factors # This returns the list of prime factors.



# This will output the list of prime factors in the correct format the problem asks for.
def output_prime_factors(prime_factors_list): # This is a function that takes prime_factor as a parameter.
    return "x".join(prime_factors_list) # This joins each value in the list with x. Each value is a string in order to use join.

# This will ask the user for n which is an integer input used in the problem.            
def user_integer_input(): # This is a function.
    while True: # This is a while loop that will keep iterating until the user inputs an integer between 1 and 10 000.
        try: # This is exception handling to prevent errors like the user inputting a string which would crash the program. Instead it outputs an error message.
            n = int(input("Enter a positive integer that is smaller than 10 000. ")) # This asks for an integer from the user which is between 1 and 10 000 for the prime factorisation.
            print() # This is just used to make the program more readable by spacing it out.
            if 1 < n <= 10000: # If the input from the user is between 1 and 10 000 (2 <= n <= 10 000), it will return the value n and exit from the function.
                return n # This returns the value n and then exits the function.
            elif n == 1: # If the user inputs 1, it will output the message below.
                print("1 does not have any prime factors. ") # This outputs a string confirming that 1 does not have any prime factors (1 is not a prime factor.)
                print() # For readability
        except: # If the input from the user causes an error that crashes the program it will output an error message
            print() # For readability.
            print("Incorrect!") # This is the error message.
            print() # For readability.
    


n = user_integer_input() # This calls the function_integer_input which is used to get an integer value from the user that is between 1 < n <= 10 000.

prime_list = prime_number_list_generator(n) # This calls the function prime_number_list_generator with the value input from the user. It stores it in the variable.
prime_factors_list = prime_factorisation_of_a_number(n, prime_list) # This calls the function prime_factorisation_of_a_number with the value from the user and the list of prime numbers. It stores it in the variable.

print(output_prime_factors(prime_factors_list)) # This outputs the prime factors with the correct format that uses the value from prime_factors_list.

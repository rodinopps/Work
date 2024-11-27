# Problem 1 - Rodin Opuz
# This is the sequence. I called it the Roro sequence. There are 6 main rules and 12 sub-rules underneath.
# There are 18 overall rules.
# The number starts with 3 and 7. The sequence is kind of inspired by FizzBuzz problems where it checks if numbers are divisible by 5 or 3.
print(""" My Sequence, My Rule - (Roro Sequence) - 3 and 7 = ?

    1. If it is divisible by 7 and 3 - It is the absolute value of the sum of squares of the two previous numbers
       subtracted by the square of the sum of two previous numbers.
      • If it is also odd - Multiply it by 21.
        - If the odd number also ends with 7 or 3 - Subtract 21.
      • Instead, if it is even - Floor divide it by 21.
        - If the even number also ends with 0 - Reverse the number.

        
    2. If it is divisible by 7 - It is the sum of squares of the two previous numbers.
      • If it is also odd - Multiply it by 7.
        - If the odd number also ends with 7 - Subtract 7.
      • Instead, if it is even - Floor divide it by 7.
        - If the even number also ends with 0 - Reverse the number.


    3. If it is divisible by 3 - It is the square of the sum of two previous numbers.
      • If it is also odd - Multiply it by 3.
        - If the odd number also ends with 3 - Subtract 3.
      • Instead, if it is even - Floor divide it by 3.
        - If the even number also ends with 0 - Reverse the number.


    4. If the number does not meet any of these rules - The two previous numbers multiplied are floor divided by the the sum of the first and second.


    5. If the calculations of a number is over 1000 - It is square rooted and turned to an integer.


    6. If the number is 0 - It adds the previous two numbers.



This sequence starts with 3 and 7. It has 18 rules. 

""")


# This is a while loop that runs until the user inputs a number bigger than 2.
# This asks the user to input the length of the sequence.
# If the user inputs a number greater than 2, it exits the loop and continues with the code.
# If the user does not input a number greater than 2, it tells the user to input a number bigger than 2 and continues with the while loop.
# It uses exception handling to prevent errors from crashing the program.
while True:
    try:
        n = int(input("Enter the N amount of terms to be generated - "))
        if n > 2:
            break
    except:
        print("You have to enter a number greater than 2 to generate a sequence - ")

# These are the first and second numbers of the sequence. They are stored in the variables.
# The numbers are then stored in a list where it will be output once it reaches the length of the user input n.
first, second = 3, 7 
sequence = [first, second] 

# This runs the code n - 2 times because there are already 2 numbers that start the sequence. 
for i in range(n - 2):
    # If the last number is divisible by 21, it calculates Rule 1.
    if second % 21 == 0:
        third = abs((first ** 2 + second ** 2) - (first + second) ** 2)
        # If the number is odd, it multiplies the number by 21.
        if third % 2 == 1:
            third *= 21
            # If the number ends with 3 or 7, it subtracts the number by 21.
            if third % 10 in [3, 7]: 
                third -= 21
        # If the number is even, it floor divides the number by 21.
        else:
            third //= 21 
            # If the number ends with 0 it turns the number into a string to reverse it and then converts back into an integer.
            if third % 10 == 0:
                third = int(str(third)[::-1])
                
    # If the last number is divisible by 7, it calculates Rule 2.           
    elif second % 7 == 0:
        third = first ** 2 + second ** 2
        # If the number is odd, it multiplies the number by 7.
        if third % 2 == 1:
            third *= 7
            # If the number ends with 7, it subtracts the number by 7.
            if third % 10 == 7:
                third -= 7
        # If the number is even, it floor divides the number by 7.
        else:
            third //= 7
            # If the number ends with 0 it reverses the number.
            if third % 10 == 0:
                third = int(str(third)[::-1])

    # If the last number is divisible by 3, it calculates Rule 3.
    elif second % 3 == 0:
        third = (first + second) ** 2
        # If the number is odd, it multiplies the number by 3.
        if third % 2 == 1:
            third *= 3
            # If the number ends with 3, it subtracts the number by 3.
            if third % 10 == 3:
                third -= 3
        # If the number is even, it floor divides the number by 3.
        else:
            third //= 3
            # If the number ends with 0, it reverses the integer.
            if third % 10 == 0:
                third = int(str(third)[::-1])

    # If the last number does not meet any of the rules above, it calculates Rule 4.
    else:
        third = (first * second ) // (first + second)

    # If the calculated number is bigger than 1000, it calculates Rule 5. This is to prevent numbers being too big, too quickly.
    if third > 1000:
        third = int(third ** 0.5)

    # If the number is 0, it calculates Rule 6. This is to prevent the sequence from just becoming 0 no matter what.
    elif third == 0:
        third = first + second
        
    # After all the Rules, it adds the number to the list.
    sequence.append(third)
    # Then the first and second variables store the values of the second and third variable.
    first, second = second, third

# Once the for loop finishes, it outputs the list. It ouputs the name of the sequence, then the sequence and then indicates the end of the sequence.
print()
print("Roro Sequence")
print()
print(sequence)
print()
print("End of the Roro sequence.")
# I know this was not necessary but I just wanted to use functions from the IN0011 books and MA0009 skills since I am interested in data analysis.
# If the user wants to, they can look at the max value, min value, range and mean.
stats = input("Do you want to look at the statistics of the sequence? (Yes/No) ")
# If the user inputs yes, it will print out the statistics.
if stats.lower() == "yes":
    print(f"Max value - {max(sequence)}") # Finds the maximum value in the list
    print(f"Min value - {min(sequence)}") # Finds the minimum value in the list.
    print(f"Range - {max(sequence) - min(sequence)}") # Finds the range with biggest number - smallest number.
    print(f"Mean - {sum(sequence) / len(sequence)}") # Finds the mean by finding the total and then dividing by the amount of terms.
# This outputs if the user says no.
elif stats.lower() == "no":
    print("Thank you for using my program!")
# This outputs if the user inputs anything else.
else:
    print("???")
# These print() statements are just a preference of mine. It's easier to read for me when it is more spaced out.
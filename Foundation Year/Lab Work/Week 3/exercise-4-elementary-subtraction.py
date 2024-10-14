first_number = input("Enter first number:\n")
second_number = input("Enter second number:\n")
first_digit, second_digit, third_digit, borrow = 0, 0, 0, 0
if first_number < second_number:
    print("First number should be greater")
else:
    if int(first_number[2])<int(second_number[2]):
        third_digit = 10 + int(first_number[2]) - int(second_number[2])
        borrow = 1
    else:
        third_digit = int(first_number[2])-int(second_number[2])
    if int(first_number[1])<int(second_number[1]):
        second_digit = 10 + int(first_number[1]) - int(second_number[1])-borrow
        borrow = 1
    else:
        second_digit = int(first_number[1])-int(second_number[1]) - borrow
        borrow = 0
    first_digit = (int(first_number[0])-int(second_number[0])-borrow)
    if first_digit == 0:
        if second_digit == 0:
            print(f"The result is: {third_digit}")
        else:
            print(f"The result is: {second_digit}{third_digit}")
    else:
        print(f"The result is: {first_digit}{second_digit}{third_digit}")
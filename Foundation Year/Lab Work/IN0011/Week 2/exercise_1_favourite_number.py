import random
while True:
    number = int(input("Enter your favourite number between 1 and 100: "))
    if 1 <= number <= 100:
        num1 = random.randint(1, number)
        num2 = number - num1
        print(f"{num2} + {num1} = {number}")
        print(f"{number + number + num1 } - {num1 + number} = {number}")

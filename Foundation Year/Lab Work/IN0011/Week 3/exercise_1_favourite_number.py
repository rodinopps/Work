import random
while True:
    num = int(input("Enter a number between 1 and 100 that is not a prime number. "))
    prime = False
    for i in range(2, num):
        if num % i == 0:
            prime = True

    if 1 <= num <= 100 and prime:
        num1 = random.randint(1, num)
        num2 = num - num1
        print(f"{num2} + {num1} = {num}")
        
        num3 = random.randint(num, 100)
        num4 = num3 - num
        print(f"{num3} - {num4} = {num}")
        
        num5 = random.randint(num, 100)
        num6 = num5 / num
        print(f"{num5} / {num6} = {num}")
        
        num7 = random.randint(1, num)
        num8 = num / num7
        print(f"{num7} * {num8} = {num}")
        
        break

    else:
        print("Try Again")

import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

disc = b ** 2 - 4 * a * c

if disc < 0:
    print("No real solutions. ")
elif disc == 0:
    one = -b / ( 2 * a)
    print(f"There is only one solution {one}")
else:
    plus = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    minus = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print(plus, minus)
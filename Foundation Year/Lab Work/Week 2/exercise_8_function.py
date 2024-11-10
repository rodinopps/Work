import math

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

if x == y:
    print(math.e ** (x ** 2 + 1))
elif x - 4 > y:
    print(x ** 3 + 3 )
else:
    print(min(x, y))

import math

def quadfunc(a, b, c):
    plus = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    minus = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return plus, minus

one = int(input("Enter a: "))
two = int(input("Enter b: "))
three = int(input("Enter c: "))
print(quadfunc(one, two, three))
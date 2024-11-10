import math
pi = 3.141592

while True:
    a = float(input("Enter major axis: "))
    b = float(input("Enter minor axis: "))
    if a > b:   
        h = (a - b) ** 2 / (a + b) ** 2
        p = pi * (a + b) * (a + (3 * h) / 10 + math.sqrt(4 - 3 * h))
        print(h, p)
    else:
        print("The major axis must be larger than the minor axis. ")


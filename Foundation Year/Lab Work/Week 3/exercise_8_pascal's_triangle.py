import math
n = int(input("Enter the value of n: "))
i = 0
while i < n:
    j = 0
    while j < (n - i + 1):
        print(end = " ")
        j += 1
    j = 0
    while j < (i + 1):
        print(math.factorial(i) // (math.factorial(j) * math.factorial(i - j)), end = " ")
        j += 1

    print()
    i += 1

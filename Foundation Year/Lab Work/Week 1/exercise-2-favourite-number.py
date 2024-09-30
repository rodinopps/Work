def favnumber():
    second = 10
    while True:
        even = int(input("Enter your favourite even number between 2 and 100: "))
        if even % 2 == 0:
            return even + second, even - second, even / second
        else:
            continue

print(favnumber())
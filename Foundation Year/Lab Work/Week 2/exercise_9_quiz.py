test = 0
number = int(input("What is 9 + 10? "))
if number == 21:
    test += 1
    print("YAY")
else:
    print("WRONG")

text1 = input("Who's the hero of time? ")
if text1.lower() == "link":
    test += 1
    print("YAY")
else:
    print("WRONG")

text2 = input("Where is clock town? ")
if text2.lower() == "termina":
    test += 1
    print("YAY")
else:
    print("WRONG")

text3 = input("What's my name? ")
if text3.lower() == "roro":
    test += 1
    print("YAY")
else:
    print("WRONG")

select = input("Which of these choices are correct? A) Apple, B) Banana, or C) Carrot?")
if select.lower == "a":
    test += 1
    print("YAY")
else:
    print("WRONG")

print(f"{test / 5 * 100}%")

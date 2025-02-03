lower = input("Enter a string: ")
upper = ""
letters = ""
for i in lower.lower():
    if i in "abcdefghijklmnopqrstuvwxyz":
        upper += chr(ord(i) - 32)
print(upper)

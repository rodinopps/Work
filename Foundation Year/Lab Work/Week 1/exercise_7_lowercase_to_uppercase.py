lower = input("Enter a string: ")
upper = ""
for i in lower:
    upper += chr(ord(i) - 32)
print(upper)


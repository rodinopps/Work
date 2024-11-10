lower = input("Enter a string: ")
upper = ""
for i in lower.lower():
    upper += chr(ord(i) - 32)
print(upper)


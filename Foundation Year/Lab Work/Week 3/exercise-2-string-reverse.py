check = input("Enter a string: ")
string = ""
for i in range(len(check) - 1, -1, -1):
    string += check[i]
print(string)
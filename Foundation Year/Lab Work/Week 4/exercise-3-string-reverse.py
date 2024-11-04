while True:
    string = input("Enter a string or quit: ")
    if string == "quit":
        break
    else:
        print(string[::-1])

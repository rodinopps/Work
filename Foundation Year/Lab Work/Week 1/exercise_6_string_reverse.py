while True:
    ten = input("Enter a string with 10 characters long: ")
    if len(ten) != 10: continue
    else:
        print(ten[::-1])
        break

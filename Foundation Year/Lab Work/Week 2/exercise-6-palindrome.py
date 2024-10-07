check = input("Enter a 5 character string: ")
if len(check) == 5 and check == check[::-1]:
    if check == check[::-1]:
        print("It is a palindrome. ")
    else:
        print("It is not a palindrome. ")
else:
    print("Wrong length of string. Try again. ")
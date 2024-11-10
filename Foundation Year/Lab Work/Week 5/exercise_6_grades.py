student = {}
while True:
    remove = input("Do you want to remove a value? If yes input the name, if no input no: ")
    print()
    
    if remove == "no":
        name = input("Enter your name: ")
        grade = int(input("Enter your grade: "))
        student[name] = grade
    else:
        if remove in student:
            student.pop(remove)
        else:
            print(f"There is no student {remove} in the dictionary")

    quit = input("Do you want to continue? Yes or no: ")
    print()
    if quit == "no":
        break

total = 0
for i in student:
    total += student[i]

print(student)
print(f"The average grade is {total / len(student)}")

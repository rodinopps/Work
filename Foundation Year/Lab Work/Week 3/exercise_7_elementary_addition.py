one = input("Enter a number: ")
two = input("Enter a number: ")
last = int(one[2]) + int(two[2])
if last >= 10:
    middle = int(one[1]) + int(two[1]) + last // 10
    if middle >= 10:
        first = int(one[0]) + int(two[0]) + middle // 10
        print(str(first) + str(middle % 10) + str(last % 10))
    else:
        first = int(one[0]) + int(two[0])
        print(str(first) + str(middle % 10) + str(last % 10))
else:
    middle = int(one[1]) + int(two[1])
    if middle >= 10:
        first = int(one[0]) + int(two[0]) + middle // 10
        print(str(first) + str(middle % 10) + str(last % 10))
    else:
        first = int(one[0]) + int(two[0])
        print(str(first) + str(middle % 10) + str(last % 10))

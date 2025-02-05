sum, count = 0, 0
while True:
    num = int(input("Enter a number between 1 and 10. "))
    if 1 <= num <= 10:
        count += 1
        sum += num
    if num == -1:
        print(count, sum)
        break

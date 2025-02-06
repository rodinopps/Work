quiz1 = int(input("Enter percentage of Quiz 1: "))
quiz2 = int(input("Enter percentage of Quiz 2: "))
demo = int(input("Enter percentage of Demo: "))
report = int(input("Enter percentage of Report: "))

percent = quiz1 * 0.15 + quiz2 * 0.15 + demo * 0.3 + report * 0.4
print (f"Total mark is {percent:.2f}")

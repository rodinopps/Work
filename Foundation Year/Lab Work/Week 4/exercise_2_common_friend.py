my_friend1 = ["Alice", "Ayesha", "Eve", "Trent"]
my_friend2 = ["Mallory", "Carol", "Adebayo", "Alice"]
common = []
for i in my_friend1:
    if i in my_friend2:
        common.append(i)

if len(common) == 0:
    print("There is no common friends between the two friend lists. ")
else:
    print(common)

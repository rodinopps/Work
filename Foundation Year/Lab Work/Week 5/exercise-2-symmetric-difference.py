set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
set3 = set()
for i in set1:
    if i not in set2:
        set3.add(i)
for i in set2:
    if i not in set1:
        set3.add(i)
print(set3)

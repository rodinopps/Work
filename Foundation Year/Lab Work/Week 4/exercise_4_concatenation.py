my_list1 = ["M", "na", "i", "Jo"]
my_list2 = ["y", "me", "s", "hn"]
new = []

minimum = min(len(my_list1), len(my_list2))

for i in range(minimum):
    new.append(my_list1[i] + my_list2[i])

if len(my_list1) > minimum:
    new.extend(my_list1[minimum:])

else:
    new.extend(my_list2[minimum:])
        
print(" ".join(new))

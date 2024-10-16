n = int(input("Enter length of sequence"))

n1, n2 = 0, 1

count = 0
while count <= n:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

    

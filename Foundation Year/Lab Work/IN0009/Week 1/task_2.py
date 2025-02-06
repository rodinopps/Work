def find_max(numbers):
    max = numbers[0]
    for i in numbers:
        if max < i:
            max = i
    return f"The maximum value is {max}. "
    
def find_min(numbers):
    min = numbers[0]
    for i in numbers:
        if min > i:
            min = i
    return f"The minimum value is {min}. "

print(find_max([12, 45, 7, 89, 23, 5]))
print(find_min([12, 45, 7, 89, 23, 5]))
print([12, 45, 7, 89, 23, 5])

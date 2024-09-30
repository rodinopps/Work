'''first_var = 5
second_var = 10
temp_var = first_var
first_var = second_var
second_var = temp_var'''

first, second = 1, 99
print(first, second)
first, second = second, first
print(first, second)

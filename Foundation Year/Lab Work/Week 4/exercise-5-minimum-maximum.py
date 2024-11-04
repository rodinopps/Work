module = ["Maths", "Python", "Computer fundamentals", "Employability"]
grade = [99, 90, 54, 67]

high = grade.index(max(grade))
low = grade.index(min(grade))

print(f"Highest grade - {module[high]}: {grade[high]}")
print(f"Lowest grade - {module[low]}: {grade[low]}")

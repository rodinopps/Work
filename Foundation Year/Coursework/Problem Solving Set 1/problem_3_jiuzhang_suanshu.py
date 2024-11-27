# Problem 3 - Rodin Opuz
# This is my program. I made a scenario to link the three unknown variables.
'''
Trick or Treat problem!
There are three types of treats in a specifc neighbourhood on Halloween. There are 3 children and each one have their
own bucket for treats. X represents a bag of jellybeans, Y represents a chocolate bar and Z represents a Lollipop.

• The 1st kid has 6 bags of jellybeans, 2 chocolate bars and 5 lollipops. The total weight of the 1st bucket is 9 units.

• The 2nd kid has 3 bags of jellybeans, 1 chocolate bar and 7 lollipops. The total weight of the 2nd bucket is 5 units.

• The 3rd kid has 4 bags of jellybeans, 3 chocolate bars and 1 lollipop. The total weight of the 3rd bucket is 7 units.

X variable = A bag of jellybeans
 - It weighs 52/45 units.
 
Y variable = A chocolate bar
 - It weighs 34/45 units.
 
Z variable = A lollipop
 - It weights 1/9 units.

I decided with this described problem because it was Halloween recently.

TLDR - Three buckets with three different treats and each bucket has different weights.
'''
# These are the three equations.
# 6x + 2y + 5z = 9
# 3x + y + 7z = 5
# 4x + 3y + z = 7

# This is a 2D list for the coefficients of each equation.
matrix = [[6, 2, 5], # First equation
          [3, 1, 7], # Second equation
          [4, 3, 1]] # Third equation

constant = [9, 5, 7] # These are the constants

# The equation is (X1 * Y2 * Z3 -  X1 * Z2 * Y3) + (Y1 * Z2 * X3 - Y1 * X2 * Z3) + (Z1 * X2 * Y3 - Z1 * Y2 * X3)
# I split the equations in the brackets into three parts and stored them in three variables and then added them up after.
# I just found it easier to do it like this instead of doing it all in one go.
# 1st - (X1 * Y2 * Z3 -  X1 * Z2 * Y3)
# 2nd - (Y1 * Z2 * X3 - Y1 * X2 * Z3)
# 3rd - (Z1 * X2 * Y3 - Z1 * Y2 * X3)

# This is the calculation of the denominator for the three equations.
bottom1 = matrix[0][0] * matrix[1][1] * matrix[2][2] - matrix[0][0] * matrix[1][2] * matrix[2][1] # First part
bottom2 = matrix[0][1] * matrix[1][2] * matrix[2][0] - matrix[0][1] * matrix[1][0] * matrix[2][2] # Second part
bottom3 = matrix[0][2] * matrix[1][0] * matrix[2][1] - matrix[0][2] * matrix[1][1] * matrix[2][0] # Third part
bottom = bottom1 + bottom2 + bottom3 # I added the three parts together to find the denominator.



# This is the calculation of the numerator for X.
top_x1 = constant[0] * matrix[1][1] * matrix[2][2] - constant[0] * matrix[1][2] * matrix[2][1] # First part
top_x2 = matrix[0][1] * matrix[1][2] * constant[2] - matrix[0][1] * constant[1] * matrix[2][2] # Second part
top_x3 = matrix[0][2] * constant[1] * matrix[2][1] - matrix[0][2] * matrix[1][1] * constant[2] # Third part
top_x = top_x1 + top_x2 + top_x3 # I added the three parts together to find the numerator for X.
x = top_x / bottom # This is the value of X.



# This is the calculation of the numerator for Y.
top_y1 = matrix[0][0] * constant[1] * matrix[2][2] - matrix[0][0] * matrix[1][2] * constant[2] # First part
top_y2 = constant[0] * matrix[1][2] * matrix[2][0] - constant[0] * matrix[1][0] * matrix[2][2] # Second part
top_y3 = matrix[0][2] * matrix[1][0] * constant[2] - matrix[0][2] * constant[1] * matrix[2][0] # Third part
top_y = top_y1 + top_y2 + top_y3 # I added the three parts together to find the numerator for Y.
y = top_y / bottom # This is the value of Y.



# This is the calculation of the numerator for Z.
top_z1 = matrix[0][0] * matrix[1][1] * constant[2] - matrix[0][0] * constant[1] * matrix[2][1] # First part
top_z2 = matrix[0][1] * constant[1] * matrix[2][0] - matrix[0][1] * matrix[1][0] * constant[2] # Second part
top_z3 = constant[0] * matrix[1][0] * matrix[2][1] - constant[0] * matrix[1][1] * matrix[2][0] # Third part
top_z = top_z1 + top_z2 + top_z3 # I added the three parts together to find the numerator for Z.
z = top_z / bottom # This is the value of Z.

# These print out the results. How much each treat weighs.
print(f"A bag of jellybeans weighs {x} units. - (52/45 units)")
print()
print(f"A chocolate bar weighs {y} units. - (34/45 units)")
print()
print(f"A lollipop weighs {z} units. - (1/9 units)")

# Problem 5 - Rodin Opuz
# Patterns
# I haven't been able to complete this but this is what I have done.
# This is based on Conway's Game of Life.



# This is used to ask the user to continue or quit the program.
def round_simulation(): # This is a function but does not take any parameters.
    while True: # This is a while loop that will keep running until the user inputs q.
        choice = input("Press Enter to continue or q to quit the simulation. ") # This asks the user to continue or quit.
        if choice == "q": # If the user presses q, it will exit the program.
            exit() # This exits the program.
        elif choice == "": # If the user presses enter, it will print the grid.
            for i in game_grid: # This is a for loop that goes through the lists (rows) of the grid.
                print(" ".join(i)) # This formats it.
        else: # If the user has not pressed enter or q, it will output a message confirming it.
            print("You have not pressed Enter or q. ") # This is the output to the user.



# This is used to create the original grid.
def starting_grid_output(): # This is a function that does not take any parameter.
    grid = [] # This creates an empty list for the grid.
    for i in range(6): # This is a for loop that iterates 6 times. This is for the amount of rows.
        row = [] # This creates an empty list for each row.
        for j in range(6): # This is a for loop that repeats 6 times. This is for the amount of values in each row.
            row.append("0") # It appends the value 0 to the row.
        grid.append(row) # Once the for loop is done iterating, it appends to the grid and then the row goes back to being empty.
    return grid # Once the for loop is done iterating, it returns the grid.



# This is used to update the values in the grid.
def grid_update_with_seeds(game_grid, seed1, seed2, seed3): # This is a function that takes four parameters. The original grid and the three coordinates for the starting seeds.
    x1 = int(seed1[0]) # This is the x coordinate from seed 1.
    y1 = int(seed1[-1]) # This is the y coordinate from seed 1.
    if 0 <= x1 <= 5 and 0 <= y1 <= 5: # If the coordinates are between 0 and 5, it will update.
        game_grid[x1][y1] = "1" # This updates the grid with the coordinates. 0 becomes 1.
    else: # If the coordinates are outside the range, it outputs an error message.
        return "WRONG" # This is the error message.

    x2 = int(seed2[0]) # This is the x coordinate from seed 2.
    y2 = int(seed2[-1]) # This is the y coordinate from seed 2.
    if 0 <= x2 <= 5 and 0 <= y2 <= 5: # If the coordinates are between 0 and 5, it will update.
        game_grid[x2][y2] = "1" # This updates the grid with the coordinates. 0 becomes 1.
    else: # If the coordinates are outside the range, it outputs an error message.
        return "WRONG" # This is the error message for seed 2.

    x3 = int(seed3[0]) # This is the x coordinate from seed 3.
    y3 = int(seed3[-1]) # This is the y coordinate from seed 3.
    if 0 <= x3 <= 5 and 0 <= y3 <= 5: # If the coordinates are between 0 and 5, it will update.
        game_grid[x3][y3] = "1" # This updates the grid with the coordinates. 0 becomes 1.
    else: # If the coordinates are outside the range, it outputs an error message.
        return "WRONG" # This is the error message for seed 3.



print("(0-5)") # This just tells the user what the range is for the coordinates.
while True: # This is a while loop that will only stop when the user inputs three correct coordinate seeds.
    game_grid = starting_grid_output() # This stores the grid from the return value from the function.
    seed1 = input("Enter the first coordinate (x, y): ") # This asks for the coordinates in the correct format.
    if seed1[1:3] == ", " and len(seed1) == 4 and seed1[0] in "012345" and seed1[3] in "012345": # If the seed is in the correct format, it will continue.
        seed2 = input("Enter the second coordinate (x, y): ") # This asks for the second input.
        if seed2[1:3] == ", " and len(seed2) == 4 and seed2[0] in "012345" and seed2[3] in "012345" and seed2 != seed1: # If the second is the correct format and is not the same as seed 1, it will continue.
            seed3 = input("Enter the third coordinate (x, y): ") # This asks for the third input.
            if seed3[1:3] == ", " and len(seed3) == 4 and seed3[0] in "012345" and seed3[3] in "012345" and seed3 != seed2 and seed3 != seed1: # If seed 3 is the correct format and is not the same as the others, it will exit the while loop.
                break # Exits the while loop.
            else: # If the seed is wrong, it gives an error message.
                print("WRONG") # Error output
        else: # If the seed is wrong, it gives an error message.
            print("WRONG") # Error output
    else: # If the seed is wrong, it gives an error message.
        print("WRONG") # Error output

grid_update_with_seeds(game_grid, seed1, seed2, seed3) # This calls the function with the four parameters, it updates the grid with three 1s.

for i in game_grid: # This is a for loop that is used to display the grid.
    print(" ".join(i)) # Goes through each row and then correctly formats it.
round_simulation() # Calls the function to ask the user to continue or quit.

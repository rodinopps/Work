# Problem 2 - Rodin Opuz
# This imports the os, time and the random module.
# The os model is used to clear the terminal to avoid cheating in the game.
# The time module is used to temporarily show the incorrect match before the terminal is cleared.
# The random module is used to generate the grids with different symbols.
import os
import time
import random

starting_time = time.time() # This stores the time the user started.

# These are the two sets I decided to use. I think its unique and the shapes are varied so they are easier to differentiate.
# Set A is for Grid A and Set B is for Grid B.
set_a = {'■', '▲', '◆', '●', '♥', '⛊', '⧗', '⬬', '⬮', '⭓'}
set_b = {'□', '△', '◇', '○', '♡', '⛉', '⧖', '⬭', '⬯', '⭔'}

# This converts the sets into lists and sorts them so the index of each list are matching pairs.
list_a = sorted(list(set_a))
list_b = sorted(list(set_b))

# This creates a dictionary called pairs, four 2D arrays called grid_a, grid_b, game_a and game_b. Thes lists will be used to generate four grids. 
pairs, grid_a, grid_b, game_a, game_b = {}, [], [], [], []

# This initialises the 4 variables to prevent errors in the exception handling except code block.
grid_a_row, grid_a_column, grid_b_row, grid_b_column = None, None, None, None

# This is used for the for loop to iterate through each value in the lists.
length = len(list_a)



# This is a while loop that will run indefinitely until the user enters a value between 3 and 10.
while True:
    try: # Exception handling to prevent a user from crashing the program if they input a non-integer value.
        n = int(input("Enter the size of the grid between 3 and 10. ")) # This stores the input of a user to generate the dimensions of the grid.
        # If the input is greater than or equal to 3 and is less than or equal to 10, it will exit the while loop.
        if 3 <= n <= 10:
            print()
            print(f"You have entered the value {n}. It creates a {n} x {n} grid. ")
            break
        # If the input is not between 3 and 10, it will output an error message.
        else:
            print()
            print("You have entered an incorrect value. Please try again. ")
    # This will output if the input from the user would crash the program. Example: "hello world!" would cause the except block code will run.
    except:
        print()
        print("You have entered an incorrect value. Please try again. ")



# This is a for loop to assign pairs between each shape into a dictionary. Example: ● (key) will match with ○ (value) in the dictionary. 
for i in range(length):
    pairs[list_a[i]] = list_b[i]

# The cells in Grid A and Grid B will be randomly filled with symbols.
# This is a for loop to create Grid A. This is used to create the 2D array for Grid A. The for loop is used to append n rows and the nested for loop is used to append n symbols to the row.
for i in range(n):
    rows = [] # This creates an empty list for a row in grid A. 
    for j in range(n):
        rows.append(random.choice(list_a)) # This appends a random symbol from A into the rows list for n times using the random module and choice.
    grid_a.append(rows) # Once the nested for loop iterates n times, it then adds the list into the 2D array and rows becomes an empty array again for the next row.

# This is a for loop to create Grid B.
for i in range(n):
    rows = []
    for j in range(n):
        rows.append(pairs[grid_a[i][j]]) # This adds the corresponding symbol for Grid A in Grid B so that there a proper amount of pairs so the game can end if finished.
    grid_b.append(rows)

# This shuffles the rows for Grid A and Grid B using the random module.
random.shuffle(grid_a)
random.shuffle(grid_b)
# This iterates through each row and shuffles the order of the symbols in the row for Grid A
for i in grid_a:
    random.shuffle(i)
# This shuffles the symbols in each row for Grid B so Grid A and Grid B are random.
for i in grid_b:
    random.shuffle(i)

# This is used to create the grids with * symbols in it. This is so the users have to guess and match. This makes the grid for A
# This is the hidden grid and the dimensions are n x n.
for i in range(n):
    rows = []
    for j in range(n):
        rows.append("*")
    game_a.append(rows)
# Example: If the user inputs 3 for n. It will create two grids for A and B
# [[*, *, *], [*, *, *], [*, *, *]]

# This makes the grid for B with hidden symbols that are represented by *
for i in range(n):
    rows = []
    for j in range(n):
        rows.append("*")
    game_b.append(rows)

turns = 0 # This is for how many turns it takes the user to finish the game.        
total = n ** 2 # This is for how many possible matches there can be and how long the game will be. Example: 3 x 3 grid will have 9 matches.



# This is a while loop that runs until there the matches left are 0.
while total > 0:
    try: # This is for exception handling in case the user inputs a non-integer value.
        print(f"Set A symbols - {list_a}") # This prints out the 10 symbols for Grid A.
        print(f"Set B symbols - {list_b}") # This prints out the 10 symbols for Grid B.
        print() # This makes it easiee to read since it makes an empty line.
        print("......")
        print("Grid A")
        print("......")
        print()
        # This is a for loop that will print each cell seperated by spaces for A.
        for i in game_a:
            print(" ".join(i))
        
        print()
        print("......")
        print("Grid B")
        print("......")
        print()
        # This is a for loop that will print each cell seperated by spaces for B.
        for i in game_b:
            print(" ".join(i))
        print()

        grid_a_row = int(input(f"Enter the Grid A row number (1 - {n}) ")) # This asks for the grid A row coordinate.
        # If the grid A row coordinate is between 1 and n, it runs the code below.
        if 1 <= grid_a_row <= n:
            grid_a_column = int(input(f"Enter the Grid A column number (1 - {n}) ")) # This asks for the Grid A column coordinate.
            # If the grid A column coordinate is between 1 and n and the coordinates have not been revealed yet, it runs the code below.
            if 1 <= grid_a_column <= n and game_a[grid_a_row - 1][grid_a_column - 1] == "*":
                game_a[grid_a_row - 1][grid_a_column - 1] = grid_a[grid_a_row - 1][grid_a_column - 1] # This replaces the * with the corresponding symbol from the Grid A.
                print()
                print("Grid A")
                # This presents Grid A in the format I have made.
                for i in game_a:
                    print(" ".join(i))
                print()
                    
                grid_b_row = int(input(f"Enter the Grid B row number (1 - {n}) ")) # This asks for the Grid B row coordinate.
                # If grid B row coordinate is between 1 and n, it runs the code below.
                if 1 <= grid_b_row <= n:
                    grid_b_column = int(input(f"Enter the Grid B column number (1 - {n}) ")) # This asks for the Grid A column coordinate.
                    # If grid B column coordinate is between 1 and n the coordinates have not been revealed yet, it runs the code below.
                    if 1 <= grid_b_column <= n and game_b[grid_b_row - 1][grid_b_column - 1] == "*":
                        game_b[grid_b_row - 1][grid_b_column - 1] = grid_b[grid_b_row - 1][grid_b_column - 1] # This replaces the * with the corresponding symbol from Grid B.
                        print()
                        print("Grid B")
                        # This presents Grid B in the format I have made.
                        for i in game_b:
                            print(" ".join(i))
                        # If the symbol from Grid A coordinates matches with the symbol from Grid B coordinates, it adds 1 to the turn counter and subtracts 1 from the total matches left and outputs Well done!
                        if pairs[grid_a[grid_a_row - 1][grid_a_column - 1]] == grid_b[grid_b_row - 1][grid_b_column - 1]:
                            turns += 1
                            total -= 1
                            print("Well done!")
                            
                        # If the symbols from Grid A and Grid B do not match, it will add 1 to the turn counter and revert the shown symbols back to * since it is wrong.
                        else:
                            print("Wrong!")
                            turns += 1
                            game_a[grid_a_row - 1][grid_a_column - 1] = "*" # Turns Grid A symbol coordinate back to *
                            game_b[grid_b_row - 1][grid_b_column - 1] = "*" # Turns Grid B symbol coordinate back to *
                    # If you enter a Grid B column that is outside the range of the grid or coordinates that have already been revealed, outputs an error message.
                    else:
                        print(f"Enter a number between 1 and {n}. Matched coordinates cannot be used again. Please try again. ")
                        game_a[grid_a_row - 1][grid_a_column - 1] = "*" # Reverts Grid A symbol back to *
                # If you enter a Grid B row that is outside the range of the grid, outputs an error message.
                else:
                    print(f"Enter a number between 1 and {n}. Matched coordinates cannot be used again. Please try again. ")
                    game_a[grid_a_row - 1][grid_a_column - 1] = "*" # Reverts Grid A symbol back to *
            # If you enter a Grid A column that is outside the range of the grid or coordinates that have already been revealed, outputs an error message.
            else:
                print(f"Enter a number between 1 and {n}. Matched coordinates cannot be used again. Please try again. ")
        # If you enter a Grid A row that is outside the range of the grid, outputs an error message.
        else:
            print(f"Enter a number between 1 and {n}. Matched coordinates cannot be used again. Please try again. ")
    # This is for exception handling if user enters a non integer value for any coordinate.
    except:
        print(f"Enter a number between 1 and {n}. Matched coordinates cannot be used again. Please try again. ")
        # If the variables are not None as they are first initialised, it updates the symbols back to *. If it equals None, it skips it to avoid errors.
        if grid_a_row is not None and grid_a_column is not None:
            game_a[grid_a_row - 1][grid_a_column - 1] = "*"

    time.sleep(3) # This gives 3 seconds for the user to view the match before it clears the terminal.
    os.system("clear") # This clears the terminal to avoid cheating.



ending_time = time.time() # This stores the time when the user finished.
print(f"Well done! You have won in {turns} turns! It took you {int(ending_time - starting_time)} seconds! The best possible amount of turns it could have taked is {n ** 2}")

# This outputs after all the matches have been completed and outputs how many turns it took for the user to complete the game and how long it took.
# The turns and time taken are just optional things that I thought could make it more competitive.

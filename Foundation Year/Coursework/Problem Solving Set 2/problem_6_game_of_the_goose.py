# Problem 6 - Rodin Opuz
# Game of the Goose
import random # This imports the random module. This is used to roll the dice for each player.



# This is used to return the value of a six sided die roll.
def dice_roll_number(): # This is a function that does not take any parameters.
    six_sided_die_number = random.randint(1, 6) # This gets a random value between 1 and 6 (simulating a dice throw) and stores it in the variable
    return six_sided_die_number # This returns the value.



# This is used to show the grid with the players on the certain numbers. It's a 8x8 grid, 64 cells.
def game_of_the_goose_board(player): # This is a function that takes a parameter player.
    matrix = [[15, 16, 17, 18, 19, 20, 21, 22],
              [14, 39, 40, 41, 42, 43, 44, 23],
              [13, 38, 55, 56, 57, 58, 45, 24],
              [12, 37, 54, 63, 64, 59, 46, 25],
              [11, 36, 53, 62, 61, 60, 47, 26],
              [10, 35, 52, 51, 50, 49, 48, 27],
              [9, 34, 33, 32, 31, 30, 29, 28],
              [8, 7, 6, 5, 4, 3, 2, 1]]
    # This is the 8x8 grid that starts at 1 and ends at 64.
    
    for i in player: # This is a for loop that will iterate through each player.
        game_grid_number = player[i] #  This stores the position of the player.
        for j in range(8): # This iterates 8 times.
            for k in range(8): # This iterates 8 times.
                if matrix[j][k] == game_grid_number: # If the number grid matches the player's position, it will run the code below. 
                    matrix[j][k] = f"P{i}" # This will store P1 or P2, depending on the iteration at the position of the grid.

    for i in matrix: # This will iterate through each row in the matrix.
        for j in i: # This will iterate through each value in the row.
            print(j, end = "\t")  # This prints the value of the row that ends with a tab space which keeps the grid aligned.
        print() # This is for readability.
        print() # This prints an empty line (empty space) for readability.
        
    

# This is used to go round by round, to roll the dice for each player.            
def gameplay(): # This is a function that does not take any parameters.
    player = {"1": 1, "2": 1} # This is the starting position the players are at. 1 which is the bottom right of the grid 
    round = 1 # This is used to store how many rounds it takes to finish the game. It starts at round 1.
    while True: # This is a while loop that will keep running until one of the players gets a score of 64.
        print(f"Game of the Goose - Round {round}") # This prints out the name of the problem and the round it is currently on.
        
        for i in player: # This will iterate through each player, Player 1 and Player 2.
            dice_value = dice_roll_number() # This calls the function dice_roll_number and stores it in the variable.
            print() # For readability.
            print(input("Press any key to continue")) # This is used to not repeat the while loop without the user's input and so the players can roll their own dice (by pressing a key/simulated roll of a dice).
            print(f"Player {i} has rolled the dice. They have rolled a {dice_value}!") # This prints out what Player rolled the dice and what value they rolled.
            player[i] += dice_value # This adds the dice value to the player score (position on the number grid).
            
            print(f"Player {i} has a score of {player[i]}") # This prints out the value the player has. The number position on the grid.

            if player[i] > 64: # If the player has a score that is bigger than 64, it will run the code below.
                print(f"Player {i} has rolled a number that has moved them beyond 64.") # This confirms this to the players.
                player[i] = 64 - (player[i] - 64) # This updates the score by bouncing back. Example: A score of 66 will become 62.
                print(f"Their score is now {player[i]}") # This outputs the new position on the number grid.
                
            elif player[i] == 64: # If the player score (position on the grid) is 64, it will exit the program and present the winner.
                print(f"Player {i} has won in {round} turns! ") # This is the output that confirms the player that won and how many rounds it took.
                exit() # This exits the program.
        round += 1 # This adds one to the round counter because the round has ended.
        game_of_the_goose_board(player) # This calls the function and takes the parameter player (which is the position on the grid). It will be used to update the player position on the grid.
    
        
    
gameplay() # This calls the gameplay function which starts the program.
    

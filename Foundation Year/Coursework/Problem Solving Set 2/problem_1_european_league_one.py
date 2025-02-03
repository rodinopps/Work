# Problem 1 - Rodin Opuz
# European League One
# I have not been able to finish it completely, but I have done what I could.
# There are four football pots with 9 football teams in each of them with a total of 36 football teams.
import random # This imports the random module to shuffle the pots.

pot_1 = ["Manchester United", "Real Madrid", "Bayern Munich", "Barcelona", "Lazio", "Deportivo La Coruña", "Arsenal", "Juventus", "Paris Saint-Germain"] # First football pot.
pot_2 = ["Valencia", "AC Milan", "Inter Milan", "Porto", "Chelsea", "Dynamo Kyiv", "Galatasaray", "AS Monaco", "Bayer Leverkusen"] # Second football pot.
pot_3 = ["Leeds United", "Lyon", "PSV Eindhoven", "Aston Villa", "Rangers", "Feyenoord", "Anderlecht", "Olympiacos", "Panathinaikos"] # Third football pot.
pot_4 = ["Celtic", "Club Brugge", "Stuttgart", "Herfølge BK", "Helsingborgs IF", "Rosenborg", "Sturm Graz", "Sparta Prague", "1860 Munich"] # Fourth football pot.

football_team_matches = {} # This is used to store the matches for each football team.
for i in pot_1 + pot_2 + pot_3 + pot_4: # This goes through each football team in all of the pots. 36 football teams.
    football_team_matches[i] = [] # This creates an empty list for each of the football teams in the dictionary. Each key is the football team and the values are the empty lists for the football matches.
    


# This is used to display the football pots.
def display_the_four_pots(): # This is a function that does not take any parameters.
    print(f"""Pot 1 - [{", ".join(pot_1)}]

Pot 2 - [{", ".join(pot_2)}]

Pot 3 - [{", ".join(pot_3)}]

Pot 4 - [{", ".join(pot_4)}]
""")
# This prints out the pots with the football teams and without speech marks.



# This is used to shuffle the pots and draw opponents for each football team.
def draw_opponents_randomly(): # This is a function that does not take any parameters.
    random.shuffle(pot_1) # This shuffles pot 1.
    random.shuffle(pot_2) # This shuffles pot 2.
    random.shuffle(pot_3) # This shuffles pot 3.
    random.shuffle(pot_4) # This shuffles pot 4.
    
                

# This is used to print out the draws for each football team.
def show_opponents_assignment(): # This is a function that does not take any parameters.
    while True: # This is a while loop that will keep iterating until the user presses N.
        
        choice = input("Do you want to check the draw for a team? (Y/N) ") # This asks if the user wants to check the draw for a team.
        print() # This is for readability.
        if choice.upper() == "Y": # If the user inputs Y, it will run the code below.
            football_team_name = input("Enter the football team name? ") # This asks for the football team name to check its draws.
            if football_team_name not in pot_1 + pot_2 + pot_3 + pot_4: # If the input from the user is not in the list of football teams, it will run the code below.
                print(f"There is not a football team with the name {football_team_name}. ") # This confirms that there is no football team named the input from the user.
                print() # This is to make it easier to read.
            else: # If the football team name is in the list of teams, it will run the code below.
                print(football_team_matches[football_team_name]) # This prints out the draws for the football teams.
                
        elif choice.upper() == "N": # If the user presses N, it will exit the program.
            break # Exits the while loop and then this ends the program.
            
        else: # If the user does not enter Y or N, it will output a message confirming the problem.
            print("You have not entered Y or N. ") # This is the output that tells the user they have not entered Y or N.
            print() # This is to make the program easier to read.
        

display_the_four_pots() # This calls the function.
draw_opponents_randomly() # This calls the function.
show_opponents_assignment() # This calls the function.

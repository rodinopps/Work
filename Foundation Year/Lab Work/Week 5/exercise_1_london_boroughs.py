division = {
    "City of London",
    "City of Westminster",
    "Kensington and Chelsea",
    "Hammersmith and Fulham",
    "Wandsworth",
    "Lambeth",
    "Southwark",
    "Tower Hamlets",
    "Hackney",
    "Islington",
    "Camden",
    "Brent",
    "Ealing",
    "Hounslow",
    "Richmond upon Thames",
    "Kingston upon Thames",
    "Merton",
    "Sutton",
    "Croydon",
    "Bromley",
    "Lewisham",
    "Greenwich",
    "Bexley",
    "Havering",
    "Barking and Dagenham",
    "Redbridge",
    "Newham",
    "Waltham Forest",
    "Haringey",
    "Enfield",
    "Barnet",
    "Harrow",
    "Hillingdon"
}

score = 0
while True:
    choice = input("Enter division or quit: ")
    if choice.lower() == "quit":
        print(f"{score} / 33")
        break
    elif choice in division:
        division.remove(choice)
        score += 1
    if score == 33:
        print("Perfect score!")
        break

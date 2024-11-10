import random
words = {"hello": "world", "bye": "bye", "no": "yes", "a": "love"}
attempts = 5

word, definition = random.choice(list(words.items()))

while attempts > 0:
    guess = input(f"Enter your guess. Definition - {definition}: ")
    if guess == word:
        print ("You guessed it correctly!")
        break
    else:
        attempts -= 1
        print(f"Incorrect guess. You have {attempts} attempts left.")
if attempts == 0:
    reveal = input("Would you like to reveal the word?")
    if reveal == "yes":
        print(f"{word}: {definition}")
    else:
        print("Bye bye!")

import random
game = {"blue + yellow": "green", "hello": "world", "9 + 10": "21", "bye": "bye!", "mar": "lui"}
for i in range(len(game)):
    word = random.choice(game)
    print(f"{word}. Guess the word associated with it. ")
    choice = input()
    if choice == word:
        print(f"{game[word]} WELL DONE YOU GOT IT CORRECT! ")

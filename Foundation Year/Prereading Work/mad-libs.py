ad = input("Enter an adjective: ").lower()
game = input("Enter the name of an outdoor game: ").lower()
ad2 = input("Enter another adjective: ").lower()
friend = input("Enter the name of a friend: ").capitalize()
verb = input("Enter a verb ending in ing: ").lower()
ad3 = input("Enter one more adjective: ").lower()

story = (f'''It was a {ad} summer day at the beach. My friends and I were in the water playing {game}. As a {ad2} wave came closer, my friend {friend} yelled, "Look! There\'s a jellyfish {verb}!"As we got closer, we saw that the jellyfish was indeed {verb}! {friend} ran out of the water and onto the sand {friend} was afraid of {verb} jellyfish. The rest of us stayed in thewater playing {game} because {verb} jellyfish are {ad3}.''')

print(story)

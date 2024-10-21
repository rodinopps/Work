import random
available = ['Anastasia', 'Eli', 'Jamal', 'Jada', 'Theo', 'Michelle', 'Adam', 'Rhea', 'Charlie', 'Jasmine', 'Marley', 'Kenji', 'Sydney', 'Yara']
jaleesa = ["Jaleesa"]
rahim = ["Rahim"]
while len(jaleesa) < 8:
    player = random.choice(available)
    jaleesa.append(player)
    available.remove(player)
rahim.extend(available)

'''print(f"{jaleesa}, this is Jaleesa's Team. ")
print(f"{rahim}, this is Rahim's Team. ")'''
print(jaleesa)

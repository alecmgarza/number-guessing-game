import random

random_num = random.randint(1,100)
print(random_num)

player_guess = int(input("Thinking of a number between 1 and 100..."))

if player_guess > random_num:
    player_guess = int(input("Lower..."))
else: 
    player_guess = int(input("Higher"))
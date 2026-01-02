import random

random_num = random.randint(1,100)
# print(random_num)
guess_count = 5

player_guess = int(input(f"Thinking of a number between 1 and 100...({guess_count} guesses remaining)\n"))
guess_count = guess_count - 1

while guess_count > 0:
    if player_guess > random_num:
        player_guess = int(input(f"Lower...({guess_count} guesses remaining)\n"))
        guess_count = guess_count - 1
    elif player_guess < random_num:
        player_guess = int(input(f"Higher...({guess_count} guesses remaining)\n"))
        guess_count = guess_count - 1
    else:
        print("Congrats! You've guessed the correct number!")
        break

if guess_count == 0:
    print("Game over, you've run out of guesses!")
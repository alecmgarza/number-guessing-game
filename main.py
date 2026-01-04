import random

def chooseDifficulty():
    global guess_count

    difficulty = input("\nChoose your difficulty...\n" \
    "Enter 1: Easy (15 guesses)\n" \
    "Enter 2: Medium (10 guesses)\n" \
    "Enter 3: Hard (5 guesses)\n\n")

    if difficulty == "1":
        guess_count = 15
    elif difficulty == "2":
        guess_count = 10
    elif difficulty == "3":
        guess_count = 5
    else:
        print("\nPlease enter a correct key. Do not include spaces.\n\n")
        chooseDifficulty()

def guessRounds():
    global guess_count

    player_guess = int(input(f"\nThinking of a number between 1 and 100...({guess_count} guesses remaining)\n\n"))

    while guess_count > 1:
        if 100 >= player_guess > random_num:
            guess_count = guess_count - 1
            player_guess = int(input(f"\nLower...({guess_count} guesses remaining)\n\n"))
        elif 1 <= player_guess < random_num:
            guess_count = guess_count - 1
            player_guess = int(input(f"\nHigher...({guess_count} guesses remaining)\n\n"))
        elif player_guess > 100 or player_guess < 1:
            print("\nPlease make sure the number you guess is within range (1-100).\n")
            guessRounds()
        else:
            print("\nCongrats! You've guessed the correct number!")
            break

    if guess_count == 1:
        print(f"\nGame over, you've run out of guesses!\nCorrect number was {random_num}.\n\n")
        return
    
# introduced a bug where multiple out of range inputs result in Game Over message getting called multiple times

def game():
    global random_num

    chooseDifficulty()
    random_num = random.randint(1,100)
    guessRounds()

game()
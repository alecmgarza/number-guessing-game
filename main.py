import random

def chooseDifficulty():
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
        print("\nPlease enter a correct key. Do not include spaces.")
        return chooseDifficulty()

    return guess_count

def randomNum():
    random_num = random.randint(1,100)

    return random_num

def takeGuesses(guess_count, random_num):
    player_guess = input(f"\nThinking of a number between 1 and 100...({guess_count} guesses remaining)\n\n")
    guess_count = guess_count - 1

    while guess_count > 0:
        try:
            player_guess = int(player_guess)
        except ValueError:
            player_guess = input("\nPlease enter a number, not letters.\n\n")
            continue

        if player_guess > 100:
            print("\nNumber cannot be more than 100.")
            player_guess = input("\nTake another guess!\n\n")
        elif player_guess < 1:
            print("\nNumber cannot be less than 1.")
            player_guess = input("\nTake another guess!\n\n")
        elif player_guess > random_num:
            player_guess = input(f"\nGo lower...({guess_count} guesses remaining)\n\n")
            guess_count = guess_count - 1
        elif player_guess < random_num:
            player_guess = input(f"\nGo higher...({guess_count} guesses remaining)\n\n")
            guess_count = guess_count - 1
        else: 
            break

    return guess_count, player_guess, random_num

def gameOver(guess_count, player_guess, random_num):
    while guess_count == 0 and player_guess != random_num:
        try:
            player_guess = int(player_guess)
        except ValueError:
            player_guess = input("\nPlease enter a number, not letters.\n\n")
            continue
        break
    
    if player_guess == random_num:
        print("\nCongrats! You've guessed the correct number!")
    else:
        print(f"\nGame over, you've run out of guesses!\nCorrect number was {random_num}.\n")

    play_again = input("Would you like to play again? (y/n)\n\n")

    if play_again == "y" or play_again == "Y":
        game()
    elif play_again == "n" or play_again == "N":
        print("\nThanks for playing!\n")
        return
    else: 
        print("\nInvalid input entered...")
        gameOver()

def game():
    guess_count = chooseDifficulty()
    random_num = randomNum()
    guess_count, player_guess, random_num = takeGuesses(guess_count, random_num)
    gameOver(guess_count, player_guess, random_num)

game()
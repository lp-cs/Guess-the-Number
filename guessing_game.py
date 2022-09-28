"""
Project 1 - Number Guessing Game
--------------------------------

For this first project you can use Workspaces.

NOTE: If you prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
from statistics import mean, median, mode



def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Save their attempt number to a list.
    6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
    7. Ask the player if they want to play again.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    WELCOME_MESSAGE = "Welcome to **Guess** **That** **Number**"
    INSTRUCTIONS = "Instructions: Guess a number between 1 and 100!"
    attempt_list = []

    print(f"{WELCOME_MESSAGE}\n{INSTRUCTIONS}\n")
    while True:
        answer = generate_answer(1, 100)
        tries = 0
        guess_list = []
        while True:
            try:
                guess = int(input("Enter your guess: "))
                if guess == 32767:
                    print("The answer is", answer)
                    continue
            except ValueError as err:
                print(f"We ran into an issue. {err}. Please try again")
            else:
                guess_list.append(guess)
                tries += 1
                if guess == answer:
                    print("Got it")
                    break
                elif guess > 100 or guess <= 0:
                    print("Try entering a number between 1 and 100")
                elif guess > answer:
                    print("It's lower!")
                elif guess < answer:
                    print("It's higher!")
                elif guess < answer:
                    print("It's higher!")

        attempt_list.append(tries)
        display_statistics(attempt_list, tries)

        continue_playing = input("Would you like to play again? [y/n]: ")

        if continue_playing.lower() == "y":
            high_score = get_min(attempt_list)
            print(f"\n\n\nCan you beat the high score of *{high_score}*?")
            continue
        elif continue_playing.lower() == "n":
            print("Closing the game! Thanks for playing")
            break
        else:
            print("Select between y or n only")




def generate_answer(a,b):
    return random.randint(a,b)



def display_statistics(a,b):
    mean = get_mean(a)
    median = get_median(a)
    mode = get_mode(a)
    print(f"\n=+=Overall Statistics=+=\nTries: {b}\nMean: {mean}\nMedian: {median}\nMode: {mode}\n")



def get_min(a):
    return min(a)



def get_mean(a):
    return mean(a)



def get_median(a):
    a.sort()
    return median(a)



def get_mode(a):
    a.sort()
    return mode(a)



# Kick off the program by calling the start_game function.
start_game()

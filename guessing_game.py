"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random
# Create the start_game function.
# Write your code inside this function.
def start_game():
#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".
    while (True):
        print("Welcome to the Number Guessing Game!")
        print("*************************************")
        print("Try to guess the number between 1 and 100")
        print("*************************************")
        random_number = random.randint(1, 100)
        guess = int(input("Please enter a number between 1 and 100: "))
        attempts = 1
        #   4. Once the guess is correct, stop looping, inform the user they "Got it"
        #      and show how many attempts it took them to get the correct number.
        while (guess != random_number):
            if (guess > random_number):
                print("It's lower")
                guess = int(input("Please enter a number between 1 and 100: "))
                attempts += 1
            elif (guess < random_number):
                print("It's higher")
                guess = int(input("Please enter a number between 1 and 100: "))
                attempts += 1
        #   5. Let the player know the game is ending, or something that indicates the game is over.
 
        print("You got it! It took you {} attempts".format(attempts))
        play_again = input("Would you like to play again? (y/n) ")
        if (play_again.lower() == "y"):
            continue
        else:
            print("Thank you for playing!")
            break

    
# Kick off the program by calling the start_game function.
start_game()
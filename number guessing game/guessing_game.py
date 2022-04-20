"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game():
    game_over = False
    num = random.randrange(10)
    tries = 0
    print("Welcome to the Number Guessing Game!")
    while not game_over:
        guess = (input("Please guess a number between 1 and 10.\n"))
        try:
            guess = int(guess)
            if guess > 10 or guess <1:
                raise ValueError
        except ValueError:
            print("That isn't a valid guess!")
        else:
            tries += 1
            if guess == num:
                print("Got it\nYou guessed the numer in {} tries!".format(tries))
                game_over = True
            elif guess > num:
                print("It's Lower")
            elif guess < num:
                print("It's Higher")
    return tries

hi_score = start_game()
while input("Would you like to play again?(Yes/No)  ").lower() == "yes":
    print("The current best score is {} tries.".format(hi_score))
    new_score = start_game()
    if new_score < hi_score:
        hi_score = new_score
print("Thanks for playing!")
          
          
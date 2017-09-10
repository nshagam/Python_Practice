# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
# 1. Keep the game going until the user types “exit”
# 2. Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

stop = ""
guess = 0
numguess = 0
wins = 0
while stop != "exit":
    r = random.randint(1, 10)
    while guess != r:
        guess = int(input("Guess the number between 1 and 9: "))
        numguess += 1
    stop = input("Correct! Continue or exit? ")
    wins += 1

print("You won the game", wins, "times using a total of", numguess, "guesses.")








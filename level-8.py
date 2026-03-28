"""
You made it to level 8!

What happens if the player types something silly like "banana"?
Let's check if their choice is in our list, and skip the turn if it's not.

We'll use "continue" to do this. When Python sees "continue" inside a loop,
it skips the rest of the turn and jumps back to the top of the loop.
"""

import random

life = 3

while life > 0:
    choices = ["rock", "paper", "scissors"]
    playerHand = input("Enter your choice " + str(choices) + ": ")

    # Step 1: Check if the player's choice is NOT in our list of valid choices.
    # Write the following below this line:
    # if playerHand not in choices:
    #     print("Oops! That's not a valid choice. Try again!")
    #     continue


    computerHand = random.choice(choices)

    print("The computer chose " + computerHand + "!")

    if playerHand == computerHand:
        print("It's a tie!")
    elif (playerHand == "rock" and computerHand == "scissors") or \
         (playerHand == "paper" and computerHand == "rock") or \
         (playerHand == "scissors" and computerHand == "paper"):
        print("You win!")
    else:
        print("You lose!")
        life -= 1  # This is a shortcut for life = life - 1
        print("You have " + str(life) + " lives remaining.")  # str() turns a number into text

# When you're done, open level-9.py to continue!

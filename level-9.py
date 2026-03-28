"""
You made it to level 9 - the final level!

Our code is getting long! Let's clean it up by putting the winner check
into its own function. A function is a reusable block of code that you
can call by name.
"""

import random

# Step 1: Let's create a function called "check_winner" that takes two inputs and returns a result.
# Write the following below this line:
# def check_winner(playerHand, computerHand):
#     if playerHand == computerHand:
#         return "It's a tie!"
#     elif (playerHand == "rock" and computerHand == "scissors") or \
#          (playerHand == "paper" and computerHand == "rock") or \
#          (playerHand == "scissors" and computerHand == "paper"):
#         return "You win!"
#     else:
#         return "You lose!"


life = 3

while life > 0:
    choices = ["rock", "paper", "scissors"]
    playerHand = input("Enter your choice " + str(choices) + ": ")

    if playerHand not in choices:
        print("Oops! That's not a valid choice. Try again!")
        continue

    computerHand = random.choice(choices)

    print("Computer plays " + computerHand + "!")

    # Step 2: Now instead of all those if/elif/else lines, we can call our function!
    # Write "result = check_winner(playerHand, computerHand)" below this line:

    # Step 3: Print the result below this line:


    # Step 4: Check if the player lost. Write the following below this line:
    # if result == "You lose!":
    #     life -= 1
    #     print(f"You have {life} lives remaining.")

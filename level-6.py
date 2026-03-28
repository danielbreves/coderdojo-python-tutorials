"""
You made it to level 6!

Right now the game only plays once. Let's use a "while" loop to keep playing
until the player runs out of lives!

A "while" loop repeats the code inside it over and over, as long as
something is true. For example, "while life > 0" means "keep going
as long as the player has lives left".
"""

import random

life = 3

# Step 1: We need a while loop that keeps going as long as the player has lives.
# Write "while life > 0:" below this line, and make sure everything after it is indented:

    playerHand = input("Enter your choice (rock, paper, scissors): ")
    computerHand = random.choice(["rock", "paper", "scissors"])

    print("The computer chose " + computerHand + "!")

    if playerHand == computerHand:
        print("It's a tie!")
    elif (playerHand == "rock" and computerHand == "scissors") or \
         (playerHand == "paper" and computerHand == "rock") or \
         (playerHand == "scissors" and computerHand == "paper"):
        print("You win!")
    else:
        print("You lose!")
        # Step 2: When the player loses, we need to subtract 1 from their lives.
        # Write "life = life - 1" below this line:

        # Step 3: Let's tell the player how many lives they have left.
        # Write print("You have", life, "lives remaining.") below this line:

# When you're done, open level-7.py to continue!

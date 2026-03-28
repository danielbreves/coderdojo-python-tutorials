"""
You made it to level 4!

Now let's put it all together and figure out who wins!
We'll use "if" to compare the player's hand to the computer's hand.

New things in this level:
  "==" checks if two things are the same. (One "=" sets a value, two "==" compares.)
  "and" means both sides must be true at the same time.

Important: In Python, the spaces at the start of a line matter!
The code inside an "if" must be indented (moved to the right) with 4 spaces.
This is how Python knows which code belongs inside the "if".
"""

import random

choices = ["rock", "paper", "scissors"]
playerHand = input("Enter your choice (rock, paper, scissors): ")
computerHand = random.choice(choices)

print("The computer chose " + computerHand + "!")

# Step 1: First let's check if it's a tie. Write the following below this line:
# if playerHand == computerHand:
#     print("It's a tie!")


# Step 2: Now let's check if the player wins with rock. Write the following below this line:
# if playerHand == "rock" and computerHand == "scissors":
#     print("You win! Rock beats scissors!")


# Step 3: Can you figure out the other two winning combinations?
# Hint: paper beats rock, and scissors beats paper.
# Write two more "if" checks below this line:

# When you're done, open level-5.py to continue!


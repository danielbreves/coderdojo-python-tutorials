"""
You made it to level 5!

In level 4 we used separate "if" checks for each winning combination.
The problem is that Python checks every single "if" even when it already found a match!

We can use "elif" (short for "else if") to say "only check this if the one above didn't match".
And "else" at the end catches everything that's left over.

Think of it like this:
  "if" checks first.
  "elif" only checks if the one above wasn't true.
  "else" runs if nothing above was true.

One more thing: when a line of code is too long, you can put a \ at the end
to tell Python "this line continues on the next line". It's like a hyphen
when you split a word across two lines in a book.
"""

import random

playerHand = input("Enter your choice (rock, paper, scissors): ")
computerHand = random.choice(["rock", "paper", "scissors"])

print("The computer chose " + computerHand + "!")

# Step 1: Check for a tie. Write the following below this line:
# if playerHand == computerHand:
#     print("It's a tie!")


# Step 2: Now use "elif" to check all the winning combinations at once.
# Write the following below this line:
# elif (playerHand == "rock" and computerHand == "scissors") or \
#      (playerHand == "paper" and computerHand == "rock") or \
#      (playerHand == "scissors" and computerHand == "paper"):
#     print("You win!")


# Step 3: If it's not a tie and the player didn't win, the player lost.
# Write the following below this line:
# else:
#     print("You lose!")

# When you're done, open level-6.py to continue!

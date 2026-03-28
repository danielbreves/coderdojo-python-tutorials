"""
You're getting the hang of this! Level 7!

Programmers don't like to repeat themselves! But we have "rock", "paper", "scissors"
written in two places: once for the player's input and once for the computer's choice.

Let's save our options in a list variable so we only write them once!

One new thing: when we want to use a list inside a message, we need to turn it
into text first using str(). For example, str(choices) turns the list into
the text "['rock', 'paper', 'scissors']".
"""

import random

life = 3

while life > 0:
    # Step 1: Let's put our options in a list called "choices".
    # Write choices = ["rock", "paper", "scissors"] below this line:


    # Step 2: Now let's use "choices" in the input message.
    # Write playerHand = input("Enter your choice " + str(choices) + ": ") below this line:


    # Step 3: Now let's use "choices" for the computer's pick too.
    # Write computerHand = random.choice(choices) below this line:


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

# Keep it up! Open level-8.py!

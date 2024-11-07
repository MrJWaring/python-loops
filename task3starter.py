import random

# Set a random number between 1 and 20
number = random.randint(1, 20)
guess = None

# Use a while loop to keep asking until the guess is correct
while guess != number:
    # Ask the user to enter a guess
    guess = int(input("Guess the number: "))
    
    # TODO: Check if the guess is too high, too low, or correct
    # TODO: Print the appropriate response

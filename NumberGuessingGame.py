
import random

print("Welcome to the Number Guessing Game!")

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Keep track of the number of guesses
num_guesses = 0

# Allow the user to guess up to 10 times
while num_guesses < 10:
    guess = int(input("Guess a number between 1 and 100: "))
    num_guesses += 1

    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        print(f"Congratulations, you guessed the number in {num_guesses} guesses!")
        break

if num_guesses == 10:
    print(f"Sorry, you didn't guess the number in time. The number was {number}.")




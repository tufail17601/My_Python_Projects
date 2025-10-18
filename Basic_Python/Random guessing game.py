import random


low = 1
high = 100


number = random.randint(low, high)


max_attempts = 7
attempts = 0

print("=== Number Guessing Game ===")
print(f"I'm thinking of a number between {low} and {high}.")
print(f"You have {max_attempts} chances to guess it!\n")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
    except ValueError:
        print(" Please enter a valid number!\n")
        continue

    attempts += 1

    if guess == number:
        print(f" Correct! The number was {number}.")
        print(f"You guessed it in {attempts} tries!")
        break
    elif guess < number:
        print(" Too low! Try again.\n")
    else:
        print(" Too high! Try again.\n")

# if all attempts are used
if attempts == max_attempts and guess != number:
    print(f"🫤 Out of chances! The correct number was {number}. Better luck next time!")

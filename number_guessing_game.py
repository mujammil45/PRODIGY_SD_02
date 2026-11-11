
import random
secret_number = random.randint(1, 100)
print("==============================")
print("     NUMBER GUESSING GAME")
print("==============================")

print("Guess a number between 1 and 100!")
try:
    guess = int(input("\nEnter your guess: "))
except ValueError:
    print("Please enter a valid number!")
    
attempts = 0

while True:
    guess = int(input("\nEnter your guess: "))
    attempts += 1
    if guess > secret_number:
        print("Too High! Try again.")

    elif guess < secret_number:
        print("Too Low! Try again.")

    else:
        print("Correct! You guessed the number!")
        print(f"Total attempts: {attempts}")
        break
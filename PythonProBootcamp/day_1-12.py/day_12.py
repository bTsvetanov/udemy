import random
print("""Welcome to the number guessing game!
I'm thinking of a number between 1 and 100.""")
number = random.randint(1,100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
guess = 0
while guess != number and attempts > 0:
    print(f"\nYou have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high.")
        attempts -= 1
    elif guess < number:
        print("Too low.")
        attempts -= 1
    else:
        print(f"You got it! The answer was {number}.")
if attempts == 0:
    print("You've run out of guesses, you lose.")
    print(f"The number was {number}.")
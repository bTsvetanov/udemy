import random as rd
choices = ['rock', 'paper', 'scissors']
cp_choice = rd.choice(choices)
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
if user_choice not in choices:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    print(f"Computer chose: {cp_choice}")
    if user_choice == cp_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and cp_choice == 'scissors') or \
         (user_choice == 'paper' and cp_choice == 'rock') or \
         (user_choice == 'scissors' and cp_choice == 'paper'):  
        print("You win!")
    else:
        print("You lose!")
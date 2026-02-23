import random
from data import data
guess_A = random.choice(data)
guess_B = random.choice(data)

def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'A'
    else:
        return guess == 'B'

score = 0
game_should_continue = True
while game_should_continue:
    
    while guess_A == guess_B:
        guess_B = random.choice(data)
    print(f"Compare A: {format_data(guess_A)}.")
    print("VS")
    print(f"Compare B: {format_data(guess_B)}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    a_follower_count = guess_A['follower_count']
    b_follower_count = guess_B['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
        if guess == 'A':
            guess_B = random.choice(data)
        else:            
            guess_A = guess_B
            guess_B = random.choice(data)
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")

import random
words = ["hello", "world", "python", "programming", "bootcamp"]
word_to_guess = random.choice(words)
word_length = len(word_to_guess)
guessed_letters = []
tries = 3 + word_length
for i in range(word_length):
    guessed_letters.append("_")
while True:
    print("Current word: " + " ".join(guessed_letters))
    guess = input("Guess a letter: ").lower()   
    if guess in word_to_guess:
        for index, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_letters[index] = guess
        if "_" not in guessed_letters:
            print("Congratulations! You've guessed the word: " + word_to_guess)
            break
    else:
        print("Incorrect guess. Try again.")
        tries -= 1
        if tries == 0:
            print("Sorry, you've run out of tries. The word was: " + word_to_guess)
            break
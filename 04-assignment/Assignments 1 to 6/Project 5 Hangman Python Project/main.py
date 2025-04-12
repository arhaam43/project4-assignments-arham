import random

# Word list
words = ["python", "programming", "hangman", "computer", "development", "crypto", "code"]

# Choose a random word
secret_word = random.choice(words)
guessed_word = ["_"] * len(secret_word)
attempts = 6
guessed_letters = []

# Introduction
print("Welcome to the Hangman Game!")
print("Guess the secret word one letter at a time.")
print(f"The word has {len(secret_word)} letters.")
print("You have 6 chances. Good luck!\n")

while attempts > 0:
    # Display current progress
    print("Word:", " ".join(guessed_word))
    print(f"Guessed Letters: {', '.join(guessed_letters)}")
    print(f"Remaining attempts: {attempts}")

    # User Input
    guess = input("Guess a letter: ").lower()

    # Input Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter a single letter.\n")
        continue

    # Check if the letter is already guessed
    if guess in guessed_letters:
        print("You already guessed that letter! Try again.\n")
        continue

    # Add the guessed letter to the list
    guessed_letters.append(guess)

    # Check if the guessed letter is in the secret word
    if guess in secret_word:
        print(f"Good job! '{guess}' is in the word.\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess

        # Check if the user guessed the word **right after correct guess**
        if "_" not in guessed_word:
            print("Congratulations! You guessed the word:", secret_word)
            break
    else:
        print(f"Oops! '{guess}' is not in the word.\n")
        attempts -= 1

    # If the user runs out of attempts
    if attempts == 0:
        print("Game over! You ran out of attempts.")
        print(f"The secret word was: {secret_word}")

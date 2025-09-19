import random

# Predefined list of 5 words
words = ["apple", "banana", "orange", "grape", "mango"]

# Randomly select a word
word = random.choice(words)
guessed_letters = set()
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")
print(f"The word has {len(word)} letters.\n")

while incorrect_guesses < max_incorrect:
    # Display current progress
    display = [ch if ch in guessed_letters else "_" for ch in word]
    print("Word:", " ".join(display))

    # Check if player has guessed all letters
    if "_" not in display:
        print("\nCongratulations! You guessed the word:", word)
        break

    # Player input
    guess = input("Guess a letter: ").strip().lower()

    # Validate input
    if not guess or len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    # Add guessed letter
    guessed_letters.add(guess)

    if guess in word:
        print("Good guess!\n")
    else:
        incorrect_guesses += 1
        print("Incorrect guess!")
        print(f"Remaining attempts: {max_incorrect - incorrect_guesses}\n")

# Game over if max incorrect guesses reached
if incorrect_guesses == max_incorrect:
    print("Game over! The word was:", word)

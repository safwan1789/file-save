import random

# List of music categories or genres
music_categories = ["rock", "jazz", "pop", "hip-hop", "classical", "country", "reggae", "blues"]

# Choose a random music category from the list
category_to_guess = random.choice(music_categories)

# Initialize variables for tracking the game
attempts = 3  # Number of attempts allowed

print("Welcome to the Music Category Guessing Game!")
print("You have", attempts, "attempts to guess the music category.")

# Main game loop
while attempts > 0:
    # Ask the player to guess the music category
    guess = input("Guess a music category: ").lower()
    
    if guess == category_to_guess:
        print("Congratulations! You've guessed the music category:", category_to_guess)
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect guess. You have", attempts, "attempts left.")
        else:
            print("Sorry, you've run out of attempts. The music category was:", category_to_guess)

print("Thanks for playing!")
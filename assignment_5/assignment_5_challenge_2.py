import random

def guess_the_number():
    """
    A number guessing game where the player has limited attempts to guess a random number.
    """
    print("🎯 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 50.")
    print("You have 5 attempts to guess it. Good luck!\n")
    
    # Generate random number and initialize game variables
    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 5
    guessed_correctly = False
    
    # Main game loop
    while attempts < max_attempts and not guessed_correctly:
        try:
            # Get user input with attempt counter
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess (1-50): "))
            
            # Validate input range
            if guess < 1 or guess > 50:
                print("Please enter a number between 1 and 50.\n")
                continue
            
            attempts += 1
            
            # Check guess against secret number
            if guess == secret_number:
                guessed_correctly = True
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempt(s)!")
            elif guess < secret_number:
                # Give hint about how close they are
                difference = secret_number - guess
                if difference > 10:
                    print("❄️  Way too low! Try a much higher number.\n")
                else:
                    print("📈 Too low! Try a slightly higher number.\n")
            else:
                # Give hint about how close they are
                difference = guess - secret_number
                if difference > 10:
                    print("🔥 Way too high! Try a much lower number.\n")
                else:
                    print("📉 Too high! Try a slightly lower number.\n")
                    
        except ValueError:
            print("⚠️  Please enter a valid integer number.\n")
    
    # Game over message
    if not guessed_correctly:
        print(f"💔 Game over! You've used all {max_attempts} attempts.")
        print(f"The secret number was: {secret_number}")
    
    # Play again option
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again in ['yes', 'y', 'yeah', 'sure']:
        print("\n" + "="*40)
        guess_the_number()
    else:
        print("Thanks for playing! 👋")

# Enhanced version with difficulty levels
def guess_the_number_advanced():
    """
    Advanced version with multiple difficulty levels and scoring system.
    """
    print("🎯 Advanced Guess the Number Game!")
    print("Choose your difficulty level:")
    print("1. Easy (1-20, 8 attempts)")
    print("2. Medium (1-50, 5 attempts)")
    print("3. Hard (1-100, 3 attempts)")
    
    # Difficulty selection
    while True:
        try:
            difficulty = int(input("Enter choice (1-3): "))
            if difficulty in [1, 2, 3]:
                break
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Set game parameters based on difficulty
    if difficulty == 1:
        range_min, range_max = 1, 20
        max_attempts = 8
    elif difficulty == 2:
        range_min, range_max = 1, 50
        max_attempts = 5
    else:
        range_min, range_max = 1, 100
        max_attempts = 3
    
    secret_number = random.randint(range_min, range_max)
    attempts = 0
    
    print(f"\nI'm thinking of a number between {range_min} and {range_max}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")
    
    # Game loop
    for attempt in range(max_attempts):
        try:
            guess = int(input(f"Attempt {attempt + 1}/{max_attempts}: Your guess? "))
            
            if guess < range_min or guess > range_max:
                print(f"Please enter a number between {range_min} and {range_max}.\n")
                continue
            
            if guess == secret_number:
                score = (max_attempts - attempt) * 100
                print(f"🎉 Perfect! You guessed it in {attempt + 1} attempts!")
                print(f"🏆 Your score: {score} points!")
                break
            elif guess < secret_number:
                print("Too low!", end=" ")
            else:
                print("Too high!", end=" ")
            
            # Give proximity hint on last attempt
            if attempt == max_attempts - 2:
                difference = abs(secret_number - guess)
                if difference <= 5:
                    print("You're very close!")
                elif difference <= 10:
                    print("You're getting warm...")
                else:
                    print("Still pretty far away.")
            print()
            
        except ValueError:
            print("Please enter a valid number.\n")
    else:
        print(f"💔 The number was {secret_number}. Better luck next time!")

# Run the game
if __name__ == "__main__":
    # Run basic version
    guess_the_number()
    
    print("\n" + "="*50)
    
    # Uncomment to run advanced version
    # guess_the_number_advanced()
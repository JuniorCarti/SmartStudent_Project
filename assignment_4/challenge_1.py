# Secret Number Guessing Game
secret_number = 7
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid number!")
import random

number_to_guess = random.randint(1, 100)
attempts = 0
guessed_correctly = False

print("I'm thinking of a number between 1 and 100.")

while not guessed_correctly:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            guessed_correctly = True
    except ValueError:
        print("Please enter a valid number.")
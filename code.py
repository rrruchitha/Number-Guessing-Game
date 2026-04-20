# number guessing game
#allow user to define range of numbers by entering a minimum and maximum number (lower and upper bounds)
# the system should generate a random number within the defined range
# the user should be prompted to guess the number
# after each guess, the system should provide feedback on whether the guess is too low, too high, or correct
# the game should continue until the user guesses the correct number
# limited number of trials = 5  
# after the game ends, we display the result in terms of 0/1 and also a message indicating whether the user won or lost


import random
def number_guessing_game():
    print("Welcome to the Number Guessing Game!\nYou will have 5 attempts to guess the correct number.\nLet's get started!")
    low = int(input("Enter the lower bound of the range: "))
    high = int(input("Enter the upper bound of the range: "))
    key = random.randint(low, high)
    attempts = 5
    while attempts > 0: 
        guess = int(input("Enter your guess: "))
        if guess < key:
            print("Too low! Try again.")
        elif guess > key:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the correct number!")
            print("Result: 1 (You won)")
            return
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    print("Sorry, you've run out of attempts.")
    print("Result: 0 (You lost)")   
    print(f"The correct number was: {key}")
    if abs(guess - key) <= 5:
        print("You were close! Better luck next time!")
    print("Better luck next time!")
    print("would you like to play again? (yes/no)")
    retry = input().lower()
    if retry == "yes":
        number_guessing_game()
    else:
        print("Thanks for playing!")
number_guessing_game()
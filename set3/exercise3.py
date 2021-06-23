"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nWelcome to the guessing game!")
    print("This game will ask for two numbers, What number is in your mind?")
    try:
        while True:
            lower_number = int(input("Enter a low number: "))
            high_number = int(input("Now, Enter a high number: "))
    except Exception:
        print("You have to enter a number!")
    print(f"OK then, a number between {lower_number} and {high_number}?")
    lower_number = int(lower_number)
    high_number = int(high_number)

    real_number = random.randint(lower_number, high_number)

    guessed = False

    while not guessed:
        guess_number = int(input("Guess a number: "))
        print(f"You guessed, {guess_number},")
        if guess_number == real_number:
            print(f"You got it!! It was {real_number}!")
            guessed = True
        elif lower_number > guess_number > high_number:
            print("Stick to your the boundary!")
        elif guess_number < real_number:
            print("Too small, try again!")
        else:
            print("Too big, try again!")
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())

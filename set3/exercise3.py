"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

def not_number_rejector_1(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    while True:
        try:
            x = int(input("Enter a low number: "))
        except Exception as e:
            print(f"Please try again {e}")
            continue
        else:
            return x

def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """

    while True:
        try:
            x = int(input("Now, Enter a high number: "))
            if low <= x <= high:
                return x
            else:
                print("Please try again")
        except Exception as e:
            print(f"Please try again {e}")

def not_number_rejector_2(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    while True:
        try:
            x = int(input("Guess a number: "))
        except Exception as e:
            print(f"Please try again {e}")
            continue
        else:
            return x
            

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
    low_number = not_number_rejector_1("Enter a low number: ")
    high_number = super_asker(low_number, float('inf'))
    print(f"OK then, a number between {low_number} and {high_number} ?")

    actualNumber = random.randint(low_number, high_number)
     
    while True:
        guessed_number = not_number_rejector_2("Guess a number: ")
        print(f"You guessed {guessed_number},")
        if guessed_number == actualNumber:
            print(f"You got it!! It was {actualNumber}!")
            return "You got it!"
        elif guessed_number < actualNumber:
            print("Too small, try again!")
        else:
            print("Too big, try again!")
   
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())

#!/usr/bin/env phython

import random

def main():
    """Start a number guessing game between 1 - 100."""
    print ("Guess the lie!")

    x = random.randint(1, 100)
    #x = random.vonmisesvariate(1,2)
    print(x)
    guess = None

    while x !=guess:

        guess = (input("Pick a number between 1 to 100:"))

        if x == guess:
            print("You genius!")
        else:
            print ("Try again")
       
main()

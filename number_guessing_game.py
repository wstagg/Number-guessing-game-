#This is a number guessing game where the user guesses a number between 1-100 in least tries possible.

import random
from random import randint

number =  randint(1,100)


print("Hello and welcome to the number guessing game!")
print("Are you ready to start?")
ready = input("Please enter 'y' if ready:")

def number_guessing_game(guess, number):
    while guess != number:
        if guess < number:
            print("too low, try again!")
        elif guess > number:
            print("too high, try again!")
        else:
            print("Well done you got it right!")
            break


if ready == "y":
    guess_number = input("Enter your guess!:")
    number_guessing_game(guess_number, number)




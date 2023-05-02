# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 09:22:11 2023

@author: laure
"""

import random

if __name__ == "__main__":
    numberToGuess = random.randint(1,100)
    guessedNumber = int(input("Can you guess the number? "))
    while(numberToGuess != guessedNumber):
        if numberToGuess < guessedNumber:
            print("You guessed too big!")
        elif guessedNumber < numberToGuess:
            print("You guessed too small!")
        guessedNumber = int(input("Try again! "))
    print("Yes!")
        
        
    
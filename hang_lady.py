#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 01:38:23 2017

@author: sara
"""
#import-statements here
import random
import re

# stupid comment

# Different ways to ask the user for letters in word
# Returns a string
def ask_letters():
    number = random.randrange(1, 6, 1)
    if number == 1:
        return "How many letters are in the word? \n"
    if number == 2:
        return "Number of letters? \n"
    if number == 3:
        return "How many letters? \n"
    if number == 4:
        return "What's the word? Just kidding. How many letters? \n"
    if number == 5:
        return "Number of letters in the word? \n"
    if number == 6:
        return "Let's do this! How many letters? \n"

# Different ways to tell the user they have to write an int
# Returns a string
def not_int():
    number = random.randrange(1, 3, 1)
    if number == 1:
        return "Need you to write a positive number. \n"
    if number == 2:
        return "Just a number, please. \n"
    if number == 3:
        return "Not an integer. Try again. \n"
    
# Uses predefined weights for different letters in Swe alphabet
# Returns a letter - higher prob for common letters
def letter_freq():
    number = random.randrange(0, 100000, 1) / 1000
    print("number is:", number)
    if number >= 99.979:
        return 'q'
    elif number >= 99.909:
        return 'z'
    elif number >= 99.767:
        return 'w'
    elif number >= 99.608:
        return 'x'
    elif number >= 98.994:
        return 'j'
    elif number >= 98.286:
        return 'y'
    elif number >= 96.981:
        return 'ö'
    elif number >= 95.643:
        return 'å'
    elif number >= 94.157:
        return 'c'
    elif number >= 92.622:
        return 'b'
    elif number >= 90.825:
        return 'ä'
    elif number >= 88.986:
        return 'p'
    elif number >= 87.067:
        return 'u'
    elif number >= 85.04:
        return 'f'
    elif number >= 82.95:
        return 'h'
    elif number >= 80.535:
        return 'v'
    elif number >= 77.673:
        return 'g'
    elif number >= 74.533:
        return 'k'
    elif number >= 71.062:
        return 'm'
    elif number >= 66.58:
        return 'o'
    elif number >= 61.878:
        return 'd'
    elif number >= 56.603:
        return 'l'
    elif number >= 50.786:
        return 'i'
    elif number >= 44.196:
        return 's'
    elif number >= 36.505:
        return 't'
    elif number >= 28.074:
        return 'r'
    elif number >= 19.532:
        return 'n'
    elif number >= 10.149:
        return 'a'
    else:
        return 'e'

num_guesses = []
word = []

class Game(object):
    def start_game():
        try:
            num_letters = float(input(ask_letters()))
            print("Number of letters:", num_letters)
        except ValueError:
            print("Value error message:", not_int())
            start_game()

    def first_guess():
        print(letter_freq())



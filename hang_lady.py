#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 01:38:23 2017

@author: sara
"""
#import-statements here
import random
import re

# Different ways to ask the user for letters in word
# Returns a string
def ask_letters():
    """Different ways to ask for starting letters"""
    choices = ["How many letters are in the word? \n",
               "Number of letters? \n",
               "How many letters? \n",
               "What's the word? Just kidding. How many letters? \n",
               "Number of letters in the word? \n",
               "Let's do this! How many letters? \n"]
    return random.choice(choices)

# Different ways to tell the user they have to write an int
# Returns a string
def not_int():
    """Different ways to ask for an int"""
    choices = ["Need you to write a positive number. \n",
               "Just a number, please. \n",
               "Not an integer. Try again. \n"]
    return random.choice(choices)

def prepare_game():
    """Gets number of letters"""
    num_letters = 0
    try:
        num_letters = int(input(ask_letters()))
        return num_letters
    except ValueError:
        print(not_int())
        return prepare_game()

def create_dic(num_letters):
    """Creates a suitable length dictionary"""
    i = 1
    while i <= num_letters:
        word[i] = "_"
        i += 1
    return word

def show_word(dictionary):
    """Creates a nice output to print"""
    x = 1
    numbers_under = []
    letters = dictionary.values()
    for i in letters:
        numbers_under.append(str(x))
        x += 1
    numbers_under_joined = ' '.join(numbers_under)
    letters_joined = ' '.join(letters)
    return letters_joined, numbers_under_joined

# Initializing variables
num_guesses = []
word = {}

# main (later on I might move this stuff into the class: Game.)
print("Hi awesome person! Think of a hang-lady-type word. Okay?") # greets the player
num_letters = prepare_game() # gets the length of thw word\
dictionary = create_dic(num_letters) # creates suitable length dictionary with placeholders

# Repeat following steps
presentation, numbers_under_joined = show_word(dictionary) # creates nice output from dictionary
print("\n" + presentation) # shows the word to user
print(numbers_under_joined)

     
'''
# To be continued...

def first_guess():
    print(letter_freq())



class Game(object):
    """A Hang Lady Game"""
    def __init__(self):
        
        try:
            num_letters = int(input(ask_letters())) #asks for number of letters
        except ValueError:
            print("Value error message:", not_int())
        print("Number of letters: " + str(num_letters)) # control print statement
'''
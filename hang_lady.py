#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 01:38:23 2017

@author: sara
"""
#import-statements here
import random
import re

def ask_letters():
    """Different ways to ask for starting letters"""
    choices = ["How many letters are in the word? \n",
               "Number of letters? \n",
               "How many letters? \n",
               "What's the word? Just kidding. How many letters? \n",
               "Number of letters in the word? \n",
               "Let's do this! How many letters? \n"]
    return random.choice(choices)

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
    """Creates a dictionary with same number entries as letters in word"""
    game_d = {}
    i = 1
    while i <= num_letters:
        game_d[i] = "_"
        i += 1
    return game_d

def show_word(game_d):
    """Creates a nice output to print"""
    x = 1
    numbers_under = []
    letters = game_d.values()
    for i in letters:
        numbers_under.append(str(x))
        x += 1
    numbers_under_joined = ' '.join(numbers_under)
    letters_joined = ' '.join(letters)
    return letters_joined, numbers_under_joined

def start_game():
    """Calls the first functions, to start a game"""
    name = input('Hi human person! What is your "name"?\n')
    input("Hi " + name + "! Think of a hang-lady-type word. Okay?\n (Press enter when ready)") # greets the player
    num_letters = prepare_game() # gets the length of the word
    game_d = create_dic(num_letters) # creates suitable length dictionary with "_" placeholders
    return game_d

def create_corpus():
    """ID's right len words from original corpus and creates corpus dictionary"""
    corpus_d = {} # dictionary with all words with right length
    with open('test_1000.txt', 'r') as fin:
        for line in fin:
            line = line.rstrip('\n')
            if len(line) == num_letters:
                line = line.lower()
                # print(line) # checks if the program works to this point
                if line not in corpus_d:
                    corpus_d[line] = 1
                else:
                    corpus_d[line] = corpus_d[line] + 1
            else:
                pass
    fin.close()
    return corpus_d

def letter_freq():
    """counts letter freq in corpus dictionary, returns most common letter"""
    freq_d = {} # dictionary with letters as keys and frequencies as values
    for i in corpus_d:
        entry = i * corpus_d.get(i) # counts the key, 'value' times
        for letter in entry:
            if letter not in freq_d:
                freq_d[letter] = 1
            else:
                freq_d[letter] = freq_d[letter] + 1
    frequency_list = [(k, freq_d[k]) for k in sorted(freq_d, key=freq_d.get, reverse=True)]
    # print(len(frequency_list), frequency_list)
    # print(frequency_list[0][0])
    return frequency_list[0][0]

def make_guess(most_common_letter):
    """Asks if letter's in word, creates a list with placements if yes"""
    placement_l = []
    yesno = input("Is '" + most_common_letter + "' in the word?\nAnswer 'y' or 'n'\n")
    if yesno.strip() == "y" or yesno == "Y":
        placement_question = input("Where in the word is the letter? Write the number, or numbers - separated by whitespace - if it's in more than one place.\n")
        placement_l = placement_question.split()
        return placement_l
    else:
        pass #this has to be changed later

def mod_game_d():
    """Modifies the game dictionary with any new correct letters"""
    for i in placement_l:
        i = int(i)
        game_d[i] = most_common_letter
        print(game_d[i])
    return(game_d)

def create_regexp():
    """Creates first regexp"""
    regexp_l = []
    for k,v in game_d.items():
        if v == "_":
            regexp_l.append(".")
        else:
            regexp_l.append(v)
    regexp = "".join(regexp_l)
    print(regexp)
    return regexp

def mod_corpus_d():
    

# Initializing variables
num_guesses = []

# main (later on I might move this stuff into the class: Game.)
game_d = start_game() # initiates, created 
num_letters = len(game_d)
corpus_d = create_corpus()
most_common_letter = letter_freq()
# make_guess(most_common_letter)
    # Repeat following steps
presentation, numbers_under_joined = show_word(game_d) # creates nice output from dictionary
print("\n" + presentation) # shows the word to user
print(numbers_under_joined)
placement_l = make_guess(most_common_letter)
print(placement_l)
mod_game_d()
print(game_d)
regexp = create_regexp()

'''
# To be continued...

def make_guess(most_common_letter):
    yesno = input("Is '" + most_common_letter + "' in the word?\nAnswer 'y' or 'n'\n")
    if yesno == "y" or yesno == "Y":


yesno = input("Is '" + letter + "' in the word?\nAnswer 'yes' or 'no'\n")

placement_question = input("Where in the word is the letter? Write the number, or 
numbers - separated by whitespace - if it's in more than one place.\n")

letter_placement = []
letter_placement = placement_question.split()

for place in letter_placement:
    dictionary(letter_placement) = letter

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
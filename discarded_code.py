#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 16:33:52 2017

@author: sara
"""

# Decided to create a dictionary instead of smaller file.
def create_corpus():
    """cuts right len words from original corpus and creates smaller corpus"""
    with open('test_1000.txt', 'r') as fin:
        for line in fin:
            line = line.rstrip('\n')
            if len(line) == num_letters:
                print(line) # checks if the program works to this point
                line = line.lower()
                w_corpus.write(line + '\n')
            else:
                pass
    w_corpus.close()

def letter_freq():
    """counts letter freq in smaller corpus, returns most common letter"""
    with r_corpus as fin:
        for line in fin:
            line = line.rstrip('\n')
            for letter in line:
                if letter not in freq_d:
                    freq_d[letter] = 1
                else:
                    freq_d[letter] = freq_d[letter] + 1
    # print(freq_d)
    s = [(k, freq_d[k]) for k in sorted(freq_d, key=freq_d.get, reverse=True)]
    print(len(s), s)
    r_corpus.close()
    print(s[0][0])
    return s[0][0]

w_corpus = open('right_len_corpus.txt', 'w') # original corpus file opened to read only

'''def create_regexp():
    length = len(game_d)
    regexp = ("." * length)
    print("Regexp:", regexp)'''
    
  'test_1000.txt', 'r'
  

'''most_common_letter = letter_freq() #counts letter freq in corpus dictionary, returns most common letter
placement_l = make_guess(most_common_letter)
# print(placement_l)
mod_game_d()
# print(game_d)
regexp = create_regexp()
corpus_d = mod_corpus_d()
#and again...
most_common_letter = letter_freq() #counts letter freq in corpus dictionary, returns most common letter
placement_l = make_guess(most_common_letter)
# print(placement_l)
mod_game_d()
# print(game_d)
regexp = create_regexp()
corpus_d = mod_corpus_d()
#and again
most_common_letter = letter_freq() #counts letter freq in corpus dictionary, returns most common letter
placement_l = make_guess(most_common_letter)
# print(placement_l)
mod_game_d()
# print(game_d)
regexp = create_regexp()
corpus_d = mod_corpus_d()'''

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
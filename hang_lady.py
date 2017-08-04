#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 01:38:23 2017

@author: sara
"""
#import-statements here

import re
from hang_lady_prepare_game import game_d #dictionary with '_' as values
from hang_lady_prepare_game import corpus_d #dictionary with word as k, frequency as v

def word_output():
    presentation, numbers_under_joined = show_word(game_d) # creates nice output from dictionary
    print("\n" + presentation) # shows right number '_' to user
    print(numbers_under_joined) #shows count under each '_'

def show_word(game_d):
    """Creates output of word and '_' to print"""
    x = 1
    numbers_under = []
    letters = game_d.values()
    for i in letters:
        numbers_under.append(str(x))
        x += 1
    numbers_under_joined = ' '.join(numbers_under)
    letters_joined = ' '.join(letters)
    return letters_joined, numbers_under_joined

def letter_freq():
    """counts letter freq in corpus dictionary, returns most common letter"""
    freq_d = {} # dictionary with letters as keys and frequencies as values
    for i in corpus_d:
        entry = i * corpus_d.get(i) # counts the key, 'value' times
        for letter in entry:
            if letter in used_letters:
                pass
            elif letter not in freq_d:
                freq_d[letter] = 1
            else:
                freq_d[letter] = freq_d[letter] + 1
    frequency_list = [(k, freq_d[k]) for k in sorted(freq_d, key=freq_d.get, reverse=True)]
    # print(len(frequency_list), frequency_list)
    # print(frequency_list[0][0])
    if frequency_list[0][0] not in used_letters:
        used_letters.append(frequency_list[0][0])
    return frequency_list[0][0]

def make_guess(most_common_letter):
    """Asks if letter's in word, creates a list with placements if yes"""
    placement_l = [] #list of places in word where letter occurs
    yesno = input("Is '" + most_common_letter + "' in the word?\nAnswer 'yes' or 'no'\n")
    if yesno.strip() == "yes" or yesno == "YES" or yesno == "Yes":
        num_dots = regexp.count(".") #counts number of unknowned letters in word
        if num_dots == 1: #if only one unknowned letter left, and player confirmed guess
        # TODO: return something instead of placement_l to end the game!!! Done?
            return 1, "done"
        else:
            placement_question = input("Where in the word is the letter? Write the number, or numbers - separated by whitespace - if it's in more than one place.\n")
            placement_l = placement_question.split()
            return 1, placement_l
    elif yesno.strip() == "no" or yesno == "NO" or yesno == "No":
        return 0, create_miss_regexp(most_common_letter)
    else:
        print("I didn't get that.")
        return make_guess(most_common_letter)

def mod_game_d(placement_l, most_common_letter):
    """Modifies the game dictionary with any new correct letters"""
    for i in placement_l:
        i = int(i)
        game_d[i] = most_common_letter
    print(game_d[i])
    return(game_d)

def create_regexp(game_d):
    """Creates regexp for letter IN word, from game dictionary"""
    regexp_l = []
    for k,v in game_d.items():
        if v == "_":
            regexp_l.append(".")
        else:
            regexp_l.append(v)
    regexp = "".join(regexp_l)
    print("This is the regexp:", regexp)
    return regexp

def create_miss_regexp(wrong_letter):
    """Creates regexp for letter NOT in word from make_guess"""
    regexp = "[^" + wrong_letter + "]"
    print("This is the error-regexp:", regexp)
    return regexp

def mod_corpus_d(regexp, corpus_d):
    """Deletes all entries in corpus dictionary that doesn't match regexp"""
    delete_l = []
    expression = re.compile(regexp)
    for k,v in corpus_d.items():
        if not re.match(expression, k):
            delete_l.append(k)
            #print(k)
        else:
            pass
    for i in delete_l:
        del corpus_d[i]
    return corpus_d

# Initializing variables
num_guesses = 0
used_letters = []
regexp = "."

#game starts with import from hang_lady_prepare_game up top

# main
while "." in regexp:
    word_output() #presents '_' and numbers to user
    regexp = create_regexp(game_d) #creates regexp from game_d
    corpus_d = mod_corpus_d(regexp, corpus_d) #TODO not sure if this is right
    print("length of corpus:", len(corpus_d)) #remove this before exam
    if len(corpus_d) < 100:
        print(corpus_d)
    else:
        pass
    most_common_letter = letter_freq() #counts letter freq in corpus dictionary, returns most common letter
    num_guesses += 1
    print("Guess number", num_guesses)
    rightWrong, placement_l = make_guess(most_common_letter)
    # print(placement_l)
    if placement_l == "done":
        print("I WON!!! With only", num_guesses, "tries!")
        break
    else:
        if rightWrong == 1:
            #corpus_d = mod_corpus_d() #TODO not sure if this is right, haven't tried it...
            game_d = mod_game_d(placement_l, most_common_letter)
        else:
            corpus_d = mod_corpus_d(regexp, corpus_d)
print("done")

#TODO fix regexp to eliminate words with already confirmed letter in other places in word
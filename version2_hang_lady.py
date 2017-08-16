#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 16:26:37 2017

@author: sara
"""

#import-statements here
import re
from hang_lady_prepare_game import game_d #dictionary with '_' as values
from hang_lady_prepare_game import corpus_d #dictionary with word as k, frequency as v

#functions
def show_word(game_d):
    """Creates output of word and '_' to print"""
    x = 1
    numbers_under = []
    letters = game_d.values() 
    for i in letters: #for every '_' in game_d
        numbers_under.append(str(x)) #add counting numbers to list numbers_under
        x += 1
    numbers_under_joined = ' '.join(numbers_under) # creates str with numbers separated by whitespace
    letters_joined = ' '.join(letters) # creates str with '_" separated by whitespace
    return letters_joined, numbers_under_joined

def word_output(game_d):
    letters_joined, numbers_under_joined = show_word(game_d) # creates nice output from dictionary
    print("\nThis is your word:")
    print(letters_joined) # shows right number '_' to user
    print(numbers_under_joined + "\n") #shows count under each '_'

def create_regexp(game_d):
    """Creates regexp for letter IN word, from game dictionary"""
    regexp_l = []
    for k,v in game_d.items(): #game_d = {1: '_', 2: '_' ...}
        if v == "_":
            regexp_l.append(".") #every "_" added to regexp_l as a "."
        else:
            regexp_l.append(v) #every letter added to regexp_l as the letter
    regexp = "".join(regexp_l) #creates a string from regexp_l
    return regexp #returns a regexp (type str)

def mod_corpus_d(regexp, corpus_d):
    """Deletes all entries in corpus dictionary that doesn't match regexp"""
    delete_l = []
    for k,v in corpus_d.items(): #for every line in corpus_d
        if not re.match(regexp, k): #if corpus_d key doesn't match my regular expression
            delete_l.append(k) #add the key to delete_l
        else:
            pass #if the key match the regular expression - do nothing
    for i in delete_l:
        del corpus_d[i] #delete all entries in corpus_d that correspond to item in delete_l
    return corpus_d #returns a reduced corpus_d, only containing words that matches regular expression

def letter_freq(corpus_d, used_letters):
    """counts letter freq in corpus dictionary, returns most common letter"""
    freq_d = {} # dictionary with letters as keys and frequencies as values
    for entry in corpus_d: #for every entry in corpus_d
        for letter in entry:
            if letter in used_letters: #if letter har already been guessed (this shouldn't happen?)
                pass
            elif letter not in freq_d:
                freq_d[letter] = 1 # adds entry {letter: 1}
            else:
                freq_d[letter] = freq_d[letter] + 1 #adds 1 to value = {letter: 2}(1+1)
    frequency_list = [(k, freq_d[k]) for k in sorted(freq_d, key=freq_d.get, reverse=True)] 
    #sorts freq_d after value, in reversed order. I.e. first entry = most frequent letter
    if frequency_list[0][0] not in used_letters: 
        used_letters.append(frequency_list[0][0]) #adds most frequent letter to list used_letters
    return frequency_list[0][0], used_letters

def create_miss_regexp(wrong_letter):
    """Creates regexp for letter NOT in word from make_guess"""
    regexp = "[^" + wrong_letter + "]"
    return regexp

def make_guess(most_common_letter):
    """Asks if letter's in word, creates a list with placements if yes"""
    yesno = input("Is the letter '" + most_common_letter + "' in the word?\nAnswer 'yes' or 'no'\n")
    if yesno.strip() == "yes" or yesno == "YES" or yesno == "Yes": #if answer is yes
        num_dots = regexp.count(".") #counts number of unknowned letters in regular expression
        if num_dots == 1: #if this is the last unknowned letter
            return "yes", "done"
        else: #if there are more than one unknowned letter
            placement_question = input("Where is the letter? Write the number. Or numbers, separated by whitespace, if it's in more than one place.\n")
            return "yes", placement_question
    elif yesno.strip() == "no" or yesno == "NO" or yesno == "No": #if answer is no
        return "no", create_miss_regexp(most_common_letter) #returns regular expression for wrong letter
    else: #if answer is neither yes or no
        print("\n Sorry, I didn't get that.")
        return make_guess(most_common_letter) #starts over with function make_guess

def mod_game_d(feedback, most_common_letter):
    """Modifies the game dictionary with any new correct letters"""
    placement_l = feedback.split() #creates a list of placements, from str
    for i in placement_l:
        i = int(i)
        game_d[i] = most_common_letter #replaces one or more '_' with correct letters
    return(game_d)

# Initializing variables
num_guesses = 0
used_letters = []
regexp = "."

# Main
while "." in regexp:
    word_output(game_d) #presents "_ _ _" and numbers under to player
    regexp = create_regexp(game_d) #creates regexp from game_d
    corpus_d = mod_corpus_d(regexp, corpus_d) #modifies corpus_d with regular expression
    most_common_letter, used_letters = letter_freq(corpus_d, used_letters) #counts letter freq in corpus dictionary, returns most common letter
    num_guesses += 1
    print("Guess number " + str(num_guesses) + ":") #presents number of guesses to player
    rightWrong, feedback = make_guess(most_common_letter)
    if feedback == "done":
        print("I WON!!! With only", num_guesses, "tries!")
        break
    else:
        if rightWrong == "yes":
            game_d = mod_game_d(feedback, most_common_letter) #adds new knowned letters to game_d
        elif rightWrong == "no":
            corpus_d = mod_corpus_d(feedback, corpus_d) #removes all words containing faulty letter from corpus_d
print("end")
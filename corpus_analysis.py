#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:38:52 2017

@author: sara
"""

# Frequency analysis of korpus

import re

def create_corpus():
    """ID's right len words from original corpus and creates corpus dictionary"""
    with open('test_1000.txt', 'r') as fin:
        for line in fin:
            line = line.rstrip('\n')
            if len(line) == num_letters:
                line = line.lower()
                print(line) # checks if the program works to this point
                if line not in corpus_d:
                    corpus_d[line] = 1
                else:
                    corpus_d[line] = corpus_d[line] + 1
            else:
                pass
    print(corpus_d)
    w_corpus.close()

def letter_freq():
    """counts letter freq in corpus dictionary, returns most common letter"""
    for i in corpus_d:
        entry = i * corpus_d.get(i) # counts the key, 'value' times
        print(entry)
        for letter in entry:
            if letter not in freq_d:
                freq_d[letter] = 1
            else:
                freq_d[letter] = freq_d[letter] + 1
    s = [(k, freq_d[k]) for k in sorted(freq_d, key=freq_d.get, reverse=True)]
    print(len(s), s)
    print(s[0][0])
    return s[0][0]

'''def regexpression():
    """picks the only possible words after hit"""
    with r_corpus as fin:
        #fin = re.findall(r'.....')
        for line in fin:
            print(line)'''

'''def create_regexp():
    """Transforms word-dictionary to regex"""
    regex = "str"
    '''

word = {} #created in other file, not avaliable here
num_letters = 9
w_corpus = open('right_len_corpus.txt', 'w')
r_corpus = open('right_len_corpus.txt', 'r')
freq_d = dict()
corpus_d = {}

# main
create_corpus()
letter_freq()
# regexpression()

'''to be continued:

yesno = input("Is '" + letter + "' in the word?\nAnswer 'yes' or 'no'\n")

placement_question = input("Where in the word is the letter? Write the number, or 
numbers - separated by whitespace - if it's in more than one place.\n")

letter_placement = []
letter_placement = placement_question.split()

for place in letter_placement:
    dictionary(letter_placement) = letter'''



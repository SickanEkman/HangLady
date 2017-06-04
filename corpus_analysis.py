#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:38:52 2017

@author: sara
"""

# Frequency analysis of korpus
import re
from hang_lady import create_corpus

def mod_corpus_d():
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
    print(corpus_d)

# initializing variables

regexp = "e........"
corpus_d = create_corpus()
mod_corpus_d()

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



# main

# regexpression()

'''to be continued:

yesno = input("Is '" + letter + "' in the word?\nAnswer 'yes' or 'no'\n")

placement_question = input("Where in the word is the letter? Write the number, or 
numbers - separated by whitespace - if it's in more than one place.\n")

letter_placement = []
letter_placement = placement_question.split()

for place in letter_placement:
    dictionary(letter_placement) = letter'''



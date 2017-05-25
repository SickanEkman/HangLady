#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:38:52 2017

@author: sara
"""

# Frequency analysis of korpus

import re

num_letters = 5
write_corpus = open('right_len_corpus.txt', 'w')
read_corpus = open('right_len_corpus.txt', 'r')
freq_d = dict()

def create_corpus():
    """cuts right len words from original corpus and creates smaller corpus"""
    with open('test_1000.txt', 'r') as fin:
        for line in fin:
            line = line.rstrip('\n')
            if len(line) == num_letters:
                print(line) # checks if the program works to this point
                line = line.lower()
                write_corpus.write(line + '\n')
            else:
                pass
    write_corpus.close()

def letter_freq():
    """counts number of letters in smaller corpus"""
    with read_corpus as fin:
        for line in fin:
            line = line.rstrip('\n')
            for letter in line:
                if letter not in freq_d:
                    freq_d[letter] = 1
                else:
                    freq_d[letter] = freq_d[letter] + 1
    print(freq_d)
    s = [(k, freq_d[k]) for k in sorted(freq_d, key=freq_d.get, reverse=True)]
    print(len(s), s)
    read_corpus.close()
    return s[0][0]

def regexpression():
    """picks the only possible words after hit"""
    read_corpus = open('right_len_corpus.txt', 'r')
    with read_corpus as fin:
        #fin = re.findall(r'.....')
        for line in fin:
            #print(line)

create_corpus()
print(letter_freq())
regexpression()

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
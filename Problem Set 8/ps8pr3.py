#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ps8pr3.py - Problem Set 8, Problem 3

Markov Text Generation

"""
import random
def create_dictionary(filename):
    """ returns a dictionary key-value pairs 
        in which the key is then followed by the words that come after the key
        input filename is a string representing the name of a text file
    """
    file = open(filename, 'r')
    text = file.read()
    file.close()
    
    words = text.split()

    d = {}
    current_word = '$'
    for next_word in words:
        if current_word not in d:
            d[current_word] = [next_word]
        else:
            d[current_word] += [next_word]
        if next_word[-1] in ['!', '.', '?']:
            current_word = '$'
        else:
            current_word = next_word    
    return d

def generate_text(word_dict, num_words):
    """ used input word_dict to generate and print num_words amount of words
        input word_dict is a dictionary of words generated from create_dictionary
        input num_words is a positive integer
    """
    current_word = '$'
    for n in range(num_words):
        wordlist = word_dict[current_word]
        next_word = random.choice(wordlist)
        print(next_word, end = ' ')
        
        if next_word[-1] in ['!', '.', '?']:
            current_word = '$'
        else:
            current_word = next_word
    print()



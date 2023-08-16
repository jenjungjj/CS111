#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:48:00 2020
ps1pr5.py - Problem Set 1, Problem 5

@author: Youjung (Jenny) Jung
BU ID#:  U01171028
"""

# function last_first(values)
def last_first(values):
    """ returns a list containing the last value 
        of the original list followed by first value of original list
        input values is a list of integers, floats or strings
    """
    last = values[-1]
    first = values[0]
    return [last, first]

# function every_other(values)
def every_other(values):
    """ returns a list containing every other value from 
        the original list
        input values is a list of integers, floats, or strings
    """
    return values[0: :2]

# function begins_with(word, prefix)
def begins_with(word, prefix):
    """ returns True if string word begins with the string prefix
        input word and prefix are string values
    """
    length = len(prefix)
    return word[0: length] == prefix



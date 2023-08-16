#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 15:33:25 2020
ps1pr6.py - Problem Set 1, Problem 6

@author: Youjung (Jenny) Jung
BU ID#:  U01171028
"""

# function reverse(s)
def reverse(s):
    """ returns a string with the characters of s in reverse order
        input s is a string
    """
    return s[-1: :-1]

# function ends_match(s)
def ends_match(s):
    """ returns true if first character in s matches the last character 
        returns false if otherwise
        input s is a string
    """
    return s[0] == s[-1]

# function replace_start(values, new_start_vals)
def replace_start(values, new_start_vals):
    """ returns a list in which the values in new_start_vals have replaced
        the first n elements in the list values, where n is the length of 
        new_start_vals
        input values and new_start_vals are lists
    """
    n = len(new_start_vals)
    return new_start_vals + values[n: ]

# function adjust(s, length)
def adjust(s, length):
    """ returns a string adjusted for its new length 
        if s is too short, the return value is padded with extra copies of 
        the last character from s
        input s is a string
        input length is an integer value
    """
    if(len(s) >= length):
        return s[0:length]
    else:
        return s + (length - len(s)) * s[-1]
        


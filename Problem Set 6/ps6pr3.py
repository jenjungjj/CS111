#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 22:43:42 2020
ps6pr3.py - Problem Set 6, Problem 3

Processing Sequences With Loops

"""
# function 1
def add_spaces(s):
    """ returns a string formed by adding a space between each pair
        of letters of the input s
        input s is an arbitrary string 
    """
    result = ''
    
    for i in range(1,len(s)):
        result = result + ' ' + s[i]
    return s[0] + result 


# function 2
def merge (s1, s2):
    """ returns a new string that has been formed by merging 
        together the string inputs s1 and s2 into a single string.
        inputs s1 and s2 are strings
    """
    result = ''
    len_shorter = min(len(s1), len(s2))
    
    for i in range(len_shorter):
        if s1[i] == s2[i]:
            result += s1[i]
        else:
            result = result + s1[i] + s2[i]
            
    if len(s1) > len(s2):
        result += s1[len_shorter: ]
    elif len(s1) < len(s2):
        result += s2[len_shorter: ]
    return result 


# function 3
def contains(s, c):
    """ returns True if input s contains c 
        returns False if otherwise.
        input s is an arbitrary string 
        input c is a single character
    """
    result = True
    for i in range(len(s)):
        if s[i] == c:
            result = True
            return result 
        else:
            result = False
    return result

        


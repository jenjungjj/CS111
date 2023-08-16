#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:51:11 2020
ps2pr4.py - Problem Set 2 , Problem 4

@author: Youjung (Jenny) Jung
BU ID#: U01171028
"""

#function 1 repeat(s, n)
def repeat(s, n):
    """ returns a string in which n number of copies of given string s
        have been concatenated using recursion
        input s is a string
        input n is an integer
    """
    if n <= 0:
        return ""
    else:
        rep = repeat(s, n-1)
        return rep + s
    
# function 2 contains(s, c)
def contains(s, c):
    """ returns True if a given string s contains the character c 
        and False if otherwise using recursive tracing 
        input s is a string
        input c is a single character
    """
    if s == '':
        return False
    elif s[0] == c:
        return True
    else:
        contains_rest = contains(s[1: ],c)
        return contains_rest
        
# function 3 add(vals1, vals2)
def add(vals1, vals2):
    """ returns a new list in which each element is the sum of the elements
        in the corresponding positions of the 2 inputs using recursion
        input vals1 and vals2 are lists of numbers
    """
    if len(vals1) != len(vals2):
        return []
    elif len(vals1) == 0 or len(vals2) == 0:
        return []
    else:
        add_rest = add(vals1[1: ], vals2[1: ])
        return [vals1[0] + vals2[0]] + add_rest


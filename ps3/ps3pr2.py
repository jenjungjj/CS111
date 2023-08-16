#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 22:35:15 2020

@author: Youjung Jenny Jung
BU ID#: U01171028

ps3pr2 - Problem Set 3, Problem 2
Algorithm Design
"""
#function 1
def cube_evens_lc(values):
    """ returns a list containing cubes of even numbers 
        using list comprehensions
        input values is a list of numbers
    """
    return ([x ** 3 for x in values if x % 2 == 0])


#function 2
def cube_evens_rec(values):
    """ returns a list containing cubes of even numbers
        using recursion
        input values is a list of numbers
    """
    if len(values) == 1:
        if values[0] % 2 == 0:
            return ([values[0] ** 3])
        else:
            return []
    else:
        rest_val = cube_evens_rec(values[1:])
        if values[0] % 2 == 0:
            return [values[0] ** 3] + rest_val
        else:
            return rest_val
        
#function 3
def num_occur(c, s):
    """ returns the number of times a character c occurs in a string s
        using either recursion or list comprehension
        input c is a single character
        input s is an arbitrary string
    """
    has_c = [1 for x in s if x == c]
    return sum(has_c)

#function 4
def most_occur(c, words):
    """ returns the string in the list words
        that has the highest nunmber of occurrences of c
        input c is a single character
        input words is a list of one or more strings
    """
    occur_num = [[num_occur(c,s),s] for s in words]
    highest = max(occur_num)
    return highest[1]

#function 5
def price_string(cents):
    """ returns a string in which the price given in cents is 
        expressed as dollars and cents
        input cents is a positive integer
    """
    d = cents // 100   # compute whole number of dollars
    c = cents % 100  # compute remaining cents
    if d >  1 and c > 1:
        return str(d) + " dollars and " + str(c) + " cents"
    elif d > 1 and c == 1:
        return str(d) + " dollars and " + str(c) + " cent"
    elif d > 1 and c == 0:
        return str(d) + " dollars"
    elif d == 1 and c > 1:
        return str(d) + " dollar and " + str(c) + " cents"
    elif d == 1 and c == 1:
        return str(d) + " dollar and " + str(c) + " cent"
    elif d == 1 and c == 0:
        return str(d) + " dollar"
    elif d == 0 and c > 1:
        return str(c) + " cents"
    else:
        return str(c) + " cent"
    
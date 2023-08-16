#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:33:16 2020

ps6pr4.py - Problem Set 6, Problem 4

Choosing the Correct Type of Loop

@author: Youjung jenny jung
"""
# function 1
def log(b,n):
    """ uses a while loop to compute and return the log base b of n.
        It also prints a sequence of messages that describe the division 
        being performed.
        input b and n are integers
    """
    count = 0
    divisor = b
    while divisor > 1:
        if n == 1:
            return 0
            break
        count += 1
        divisor = n // b
        print('dividing', n, 'by', b, 'gives', divisor)
        n = divisor
    return count


# function 2
def add_powers(m,n):
    """ uses a for loop to compute and return the sum of the first m powers of n 
        from n ** 0 to n**(m-1)
        inputs m and n are integers
    """
    result = 0
    for x in range(m):
        power_val = n ** x
        result += power_val
        print(n, '**', x, '=', power_val)
    return result
        

# function 3
def negate_odds(values):
    """ replaces a list of values with a new list in which
        the odd numbers have been negated whlie the even numbers are kept the same.
        input values is a list of numbers
    """
    for i in range(len(values)):
        if values[i] % 2 == 1:
            values[i] = - values[i]
    

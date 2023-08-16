#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:42:09 2020
ps4pr3.py - Problem Set 4, Problem 3
Recursive Operations on Binary Numbers

@author: Youjung jenny jung

"""

# function 1 
def bitwise_and(b1, b2):
    """ using recursion, computes and returns the ANDed result of two string inputs b1 and b2
        which represent binary numbers 
        inputs b1 and b2 are strings representing binary numbers
    """
    if b1 == '' and b2 == '':
        return ''
    elif b1 == '':
        return '0' * len(b2)
    elif b2 == '':
        return '0' * len(b1)
    else:
        rest_bits = bitwise_and(b1[:-1], b2[:-1])
        if b1[-1] == '1' and b2[-1] == '1':
            return rest_bits + '1'
        else:
            return rest_bits + '0'

# function 2
def add_bitwise(b1, b2):
    """ returns the result of the bitwise addition algorithm of two string inputs
        using recursion
        inputs b1 and b2 are strings representing binary numbers
    """
    if b1 == '' and b2 == '':
        return ''
    elif b1 == '':
        return b2
    elif b2 == '':
        return b1
    else:
        sum_rest = add_bitwise(b1[:-1], b2[:-1])
        if b1[-1] == '0' and b2[-1] == '1':
            return sum_rest + '1'
        elif b1[-1] == '1' and b2[-1] == '0':
            return sum_rest + '1'
        elif b1[-1] == '0' and b2[-1] == '0':
            return sum_rest + '0'
        else:
            sum_rest2 = add_bitwise(sum_rest, '1')
            return sum_rest2 + '0' 
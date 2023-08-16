#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ps4pr1.py - Problem Set 4, Problem 1
From Binary to decimal and back!

@author: Youjung (Jenny) jung

"""
#function 1
def dec_to_bin(n):
    """ returns a string version of the binary representation of the input n
        using recursion to convert from decimal to binary
        input n is a non-negative integer 
    """
    if n == 1:
        return '1'
    elif n == 0:
        return '0'
    else:
        to_bin = dec_to_bin(n//2)
        if n % 2 == 1:
            return to_bin + '1'
        else:
            return to_bin + '0'
        
# function 2
def bin_to_dec(b):
    """ returns an integer of a given binary input 
        using recursion to convert from binary to decimal
        input b is a string that represents a binary number
    """
    if b == '1':
        return 1
    elif b == '0':
        return 0
    else:
        to_dec = bin_to_dec(b[0:-1])
        if b[-1] == '1':
            return 2 * to_dec + 1
        else:
            return 2 * to_dec + 0
            


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:10:19 2020
ps4pr2.py- Problem Set 4, Problem 2
Using Conversion Functions


@author: Youjung jenny jung
"""
from ps4pr1 import *
#function 1
def mul_bin(b1, b2):
    """ returns the multiplied string representation of the
        binary numbers b1 and b2.
        input b1 and b2 are strings representing binary numbers
    """
    n1 = bin_to_dec(b1)
    n2 = bin_to_dec(b2)
    b = dec_to_bin(n1 * n2)
    return b
    
#function 2
def add_bytes(b1, b2):
    """ returns the sum of two string inputs that represents bytes 
        in the form of a string that represents 8-bit binary number
    """
    n1 = bin_to_dec(b1)
    n2 = bin_to_dec(b2)
    b_sum = dec_to_bin(n1 + n2)
    if len(b_sum) <= 8:
        return '0' * (8-len(b_sum)) + b_sum 
    else:
        return b_sum[-8: -1] + b_sum[-1]
    



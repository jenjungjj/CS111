"""
Created on Tue Sep 22 22:51:27 2020

@author: Youjung Jenny Jung
BU ID#: U01171028

ps2pr3.py - Problem Set 2, Problem 3
Practicing writing non-recursive functions
"""
# function 1 move_to_end(s, n)
def move_to_end(s,n):
    """ returns a new string in which the first n characters of s 
        have been moved to the end of the old string s
        input s is a string 
        input n is an integer
    """
    replace = s[n: ]
    return replace + s[0:n]


# function 2 reverse_last(vals, n) 
def reverse_last(vals,n):
    """ returns a new list in which the last n values of
        the old list vals are placed in reverse order
        input vals is a list 
        input n is an integer
    """
    length = len(vals)
    if length >= n:
        reverse = vals[ : -(n+1): -1]
        return vals[0:length-n] + reverse
    else:
        return vals[ : 0: -1] + vals[0:1]

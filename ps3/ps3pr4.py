#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ps3pr4.py - Problem Set 3 Problem 4
More Algorithm Design
"""
#function 1
def first_occur(seq, elem):
    """ returns the index of the first occurrence of the input elem
        in a given sequence using recursive tracing
        input seq can be a list or string
        input elem is an element
    """
    if seq == [] or seq == '':
        return -1
    elif seq[0] == elem:
        return  0
    else:
        idx_count = first_occur(seq[1:], elem)
        if idx_count > len(seq):
            return idx_count
        else:
            return idx_count + 1

# function 2
def last_occur(seq, elem):
    """ returns the index of the last occurrence of the input elem 
        in a given sequence using recursive tracing 
        input seq can be a list or string
        input elem is an element
    """
    if seq == [] or seq == '':
        return -1
    elif seq[-1] == elem:
        return len(seq) - 1
    else:
        idx_count = last_occur(seq[0:-1], elem)
        return idx_count


#helper function
def rem_first(elem, values):
    """ removes the first occurrence of elem from the list values
    """
    if values == '':
        return ''
    elif values[0] == elem:
        return values[1:]
    else:
        result_rest = rem_first(elem, values[1:])
        return values[0] + result_rest    
# function 3
def jscore(s1, s2):
    """ returns the number of shared characters in inputs s1 and s2
        input s1 and s2 are strings
    """
    if s1 == '' or s2 == '':
        return 0
    else:
        removed = jscore(s1[1:], rem_first(s1[0], s2))
        if s1[0] in s2:
            return 1 + removed
        else:
            return removed
    
    
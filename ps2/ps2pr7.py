#
# ps2pr7.py - Problem Set 2, Problem 7
#
# Fun with Recursion, part 2
#
# Computer Science 111
#
# problem 7-1
def letter_score(letter):
    """ returns the value of the input letter as a scrabble tile
        returns 0 if the input is not a lowercase letter from 'a' to 'z'
        input letter is a string
    """
    assert(len(letter)== 1)
    if letter in ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']:
        return 1
    elif letter in ['d', 'g']:
        return 2
    elif letter in ['b', 'c', 'm', 'p']:
        return 3
    elif letter in ['f', 'h', 'v', 'w', 'y']:
        return 4
    elif letter in ['k']:
        return 5
    elif letter in ['j', 'x']:
        return 8
    elif letter in ['q', 'z']:
        return 10
    else:
        return 0
    
# problem 7-2
def scrabble_score(word):
    """ returns the sum of the scrabble score of the input string 
        using recursion
        input word is a string containing only lowercase letters
    """
    if len(word) == 1:
        return letter_score(word)
    else:
        remaining = scrabble_score(word[1:])
        return remaining + letter_score(word[0])
    
# problem 7 - 3
def smaller_of(vals1, vals2):
    """ returns a list in which each element is the smaller value
        between the two original lists
        input vals1 and vals2 are lists
    """
    if len(vals1) == 1 or len(vals2) == 1:
        if vals1[0] > vals2[0]:
            return vals2
        else:
            return vals1
    elif len(vals1) == 0 or len(vals2) == 0:
        return []
    else:
        smaller_vals = smaller_of(vals1[1:], vals2[1:])
        if vals1[0] > vals2[0]:
            return [vals2[0]] + smaller_vals
        else:
            return [vals1[0]] + smaller_vals

# problem 7-4
def merge(s1, s2):
    """ returns a new string that has been merged together by the characters
        in the two given strings. 
        The same characters at the same position are included once
        Different characters of the same position are both included
        input s1 and s2 are string values
    """
    if len(s1) == 0 and len(s2) == 0:
        return ''
    elif len(s1) == 0 and len(s2) != 0:
        return s2
    elif len(s1) != 0 and len(s2) == 0:
        return s1
    elif len(s1) == 1 or len(s2) == 1:
        if s1 == s2:
            return s1
        elif len(s1) > len(s2):
            return s2 + s1
        else:
            return s1 + s2
    else:
        characters = merge(s1[1:], s2[1:])
        if s1[0] == s2[0]:
            return s1[0] + characters
        else:
            return s1[0] + s2[0] + characters


        
    
    
    
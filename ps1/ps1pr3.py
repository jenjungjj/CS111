# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# name: Youjung (Jenny) Jung
# BU ID: U01171028
#
# Functions with numeric inputs
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below
# function 1
def root(x):
    """ returns the square root value of its input
        input x: any number(int or float)
    """
    return x ** 0.5

# function 2
def gap(num1, num2):
    """ returns num1 - num2 if num1 is greater than num2
        returns num2 - num1 if num2 is greater than num1
        returns 0 if num1 and num2 are equal
        input num1, num2: any number (int or float)
    """
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1
    
# funtion 3
def larger_gap(a1, a2, b1, b2):
    """ computes the gap between a1 and a2
        computes the gap between b1 and b2
        returns larger of the two gaps
        input a1, a2, b1, b2: any number (int or float)
    """
    gap1 = 0
    gap2 = 0
    if a1 > a2:
        gap1 = gap1 + (a1 - a2)
    else:
        gap1 = gap1 + (a2 - a1)
    if b1 > b2:
        gap2 = gap2 + (b1 - b2)
    else:
        gap2 = gap2 + (b2 - b1)
    if gap1 > gap2:
        return gap1
    else:
        return gap2
    
# function 4
def median(a,b,c):
    """ returns the median value of the 3 inputs
        input a, b, c: any number (int or float)
    """
    if a <= b <= c:
        return b
    elif b <= c <= a:
        return c
    elif c <= a <= b:
        return a
    elif c <= b <= a:
        return b
    elif b <= a <= c:
        return a
    else:
        return c






# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))

    # optional but encouraged: add test calls for your functions below

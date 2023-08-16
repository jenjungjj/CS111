#
# ps2pr6.py - Problem Set 2, Problem 6
#
# Writing list comprehensions
#
# Computer Science 111
#

# Problem 6-1: LC puzzles!
# This code won't work until you complete the list comprehensions!
# If you can't figure out how to complete one of them, please
# comment out the corresponding lines by putting a # at the start
# of the appropriate lines.

# part a
lc1 = [       for x in range(7)]

# part b
words = ['do', 'you', 'comprehend', 'list', 'comprehensions?']
lc2 = [       for w in words]

# part c
lc3 = [       for w in ['python', 'is', 'very', 'fun!']]

# part d
lc4 = [       for y in range(2, 8)]

# part e
lc5 = [       for c in 'abracadabra' if              ]


# Problem 6-2: Put your definition of the multiples_of() function below.



# Problem 6-3: Put your definition of the longer_than() function below.




# The code below prints the values of your expressions
# from 6-1. DO NOT MODIFY IT!
if __name__ == '__main__':    
    for n in range(1, 6):
        lc_var = 'lc' + str(n)
        if lc_var in dir():
            print(lc_var, '=', eval(lc_var))

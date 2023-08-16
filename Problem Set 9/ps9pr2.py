#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.
class Player:
    def __init__(self, checker):
        """ intializes a one-character string to the param checker
        intializes an integer that stores the nunmber of moves the player has made so far
        in the param num_moves
            """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        """ returns a string representing the Player object 
            indicating which checker the Player object is using
        """
        s = 'Player '
        return s + self.checker
    
    def opponent_checker(self):
        """ returns the opponent's checker
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, b):
        """ accepts Board object b as a param 
            returns the column where the player wants to make the next move. 
        """
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True:
                return col
            else:
                print('Try again!')
        
    



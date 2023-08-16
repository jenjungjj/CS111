#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
        
def process_move(p,b):
    """ function performs all of the steps involved in a single move by player b 
        on board b
    """
    turn = p.__repr__()
    print(turn,"'s turn")
    next_turn = p.next_move(b)
    b.add_checker(p.checker, next_turn)
    print()
    print(b)
    print()
    result = b.is_win_for(p.checker)
    if result == True:
        print(turn, 'wins in', p.num_moves, 'moves.')
        print('Congratulations!')
        return result
    elif b.is_full() == True and result == False:
        print('It\'s a tie!')
        return True
    else:
        return False
    
class RandomPlayer(Player):
    """ subclass of the Player class
        no new fields; all the attributes is inherited from Player
    """
    def next_move(self, b):
        """ replaces the next_move method inherited from Player
            returns the index of a randomly selected column where the player
            wants to make the next move.
        """
        
        self.num_moves += 1
        available_cols = [ col for col in range(b.width) if b.can_add_to(col) == True]
        col = random.choice(available_cols)
        return col
                
            

#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """ subclass of the Player class
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """ returns a string representing the AIPlayer object
        """
        s = 'Player ' + self.checker + ' '
        s += '(' + str(self.tiebreak) + ', ' + str(self.lookahead) + ')'
        return s
        
    
    def max_score_column(self, scores):
        """ returns the index of the column with the maximum score
            If more than one columns are tied for the max score, AIPlayer's 
            tiebreaking strategy is used to break the tie. 
        """
        max_score = max(scores)
        max_idx_list = []
        for x in range(len(scores)):
            if scores[x] == max_score:
                max_idx_list += [x]
        if self.tiebreak == 'LEFT':
            return max_idx_list[0]
        elif self.tiebreak == 'RIGHT':
            return max_idx_list[-1]
        else:
            return random.choice(max_idx_list)
        
        
    def scores_for(self, b):
        """ returns a list containing a score for each column. 
        """
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead -1)
                opp_scores = opponent.scores_for(b)
                if max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 100:
                    scores[col] = 0
                else:
                    scores[col] = 50
                b.remove_checker(col)
        return scores
    
    def next_move(self, b):
        """ overrides the next_move method inherited from the Player class 
            returns the AIPlayer's judgement of its best possible move 
        """
        self.num_moves += 1
        scores = self.scores_for(b)
        column = self.max_score_column(scores)
        return column
                
                
            
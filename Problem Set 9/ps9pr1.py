#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, height, width):
        """ initializes height that stores the number of rows,
            width that stores the number of columns, 
            slots that store a 2D list with height rows and width columns
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * width for r in range(height)]


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        s += '-' * (2 * self.width + 1)
        s += '\n'
        for n in range(self.width):
            indx = n % 10
            if indx == 0:
                s += ' 0'
            elif indx == 1:
                s += ' 1'
            elif indx == 2:
                s += ' 2'
            elif indx == 3:
                s += ' 3'
            elif indx == 4:
                s += ' 4'
            elif indx == 5:
                s += ' 5'
            elif indx == 6:
                s += ' 6' 
            elif indx == 7:
                s += ' 7'
            elif indx == 8:
                s += ' 8'
            else:
                s += ' 9'
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        row = 0
        while self.slots[row][col] == ' ':
            if row >= self.height - 1:
                break
            row += 1
        if self.slots[row][col] == ' ':
           self.slots[row][col] = checker
        else:
           self.slots[row - 1][col] = checker
        

    
    ### add your reset method here ###
    def reset(self):
        """ resets the Board object by having empty spaces in the slots
        """
        for r in range(self.height):
            for c in range(self.width):
                self.slots[r][c] = ' '
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    def can_add_to(self, col):
        """ returns True if a checker can be placed in the column col
            otherwise, it returns False
        """
        if col < 0 or col >= self.width:
            return False
        elif self.slots[0][col] == ' ':
            return True
        else:
            return False
            
    def is_full(self):
        """ returns True if the Board is completely full of checkers
            False if otherwise
        """
        full = True
        for c in range(self.width):
            if self.slots[0][c] == ' ':
                full = False
        return full
    
    def remove_checker(self, col):
        """ removes the top checker from the given column number col 
            of the called Board object
        """
        assert(col >= 0 and col < self.width)
        row = 0 
        while self.slots[row][col] == ' ':
            if row >= self.height - 1:
                break
            row += 1
        self.slots[row][col] = ' '
        
    def is_horizontal_win(self, checker):
        """ checks for a horizontal win for the specified checker
        """
        for row in range(self.height):
            for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False
    
    def is_vertical_win(self, checker):
        """ checks for a vertical win for the specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                       return True
        return False
    
    def is_down_diagonal_win(self, checker):
        """ checks for a diagonal downward win for the specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                       return True
        return False
    
    def is_up_diagonal_win(self, checker):
        """ checks for a diagonal upward win for the specified checker
        """
        for row in range(self.height -1 , self.height - 5 , -1):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                       return True
        return False 
    
    def is_win_for(self, checker):
        """ returns True if there are 4 consecutive checkers of the same type 
            horizontally, vertically, or diagonally
            returns False if otherwise
        """
        assert(checker == 'X' or checker == 'O')
        
        if self.is_horizontal_win(checker) == True and self.width > 3:
            return True
        elif self.is_vertical_win(checker) == True and self.height > 3:
            return True
        elif self.width > 3 and self.height > 3:
            if self.is_down_diagonal_win(checker) == True:
                return True
            elif self.is_up_diagonal_win(checker) == True:
                return True
            else:
                return False
        else:
            return False
                

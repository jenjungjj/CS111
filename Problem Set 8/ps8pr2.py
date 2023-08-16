#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# A class to represent calendar dates       
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.month = init_month
        self.day = init_day
        self.year = init_year


    # The function for the Date class that returns a string
    # representation of a Date object.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this *can* be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year, and False otherwise.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, and year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

    #### Put your code for problem 2 below. ####
    #### Make sure that it is indented by an appropriate amount. ####
    # part 3
    def advance_one(self):
        """ changes the value of one or more variables inside a called object
            by advancing the date object by one day
        """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if days_in_month[self.month] == 31:
            if self.month == 12 and self.day == 31:
                self.day = 1
                self.month = 1
                self.year += 1
            elif self.day == 31:
                self.day = 1
                self.month += 1
            else:
                self.day += 1
        elif days_in_month[self.month] == 30:
            if self.day == 30:
                self.day = 1
                self.month += 1
            else:
                self.day += 1
        elif days_in_month[self.month] == 28 and self.is_leap_year() == False:
            if self.day == 28:
                self.day = 1
                self.month = 3
            else:
                self.day += 1
        else:
            days_in_month[2] == 29
            if self.day == 29:
                self.day = 1
                self.month = 3
            else:
                self.day += 1
        
            
    # part 4            
    def advance_n(self, n):
        """ changes the calling object to represent n calendar days after the original date
        """
        if n != 0:
            for x in range(n):
                print(self)
                self.advance_one()
        print(self)
            
    # part 5        
    def __eq__(self, other):
        """ returns True if the self object and the other object have the same 
            calendar date
        """
        if self.day == other.day and self.month == other.month and self.year == other.year:
            return True
        else:
            return False
    
    # part 6
    def is_before(self, other):
        """ returns True if the date of the called object comes before the calendar date
            stored in the other object. If they have the same dates, it returns False
        """
        if self.year < other.year:
            return True
        elif self.month < other.month and self.year <= other.year:
            return True
        elif self.day < other.day and self.month <= other.month and self.year <= other.year:
            return True
        else:
            return False
        
    # part 7
    def is_after(self, other):
        """ returns True if the date of the called object comes after the calendar date
            stored in the other object. If they have the same dates, it returns False
        """
        if self.is_before(other) == True:
            return False
        elif self.__eq__(other) == True:
            return False
        else:
            return True
        
    # part 8
    def days_between(self, other):
        """ returns an integer that represents the number of days between self and other
        """
        self1 = self.copy()
        other1 = other.copy()
        count = 0
        if self.is_before(other) == True:
            while self1.is_before(other1) == True:
                count -= 1
                self1.advance_one()
        elif self.is_after(other) == True:
            while self1.is_after(other1) == True:
                count += 1
                other1.advance_one()
        else:
            count = 0
        return count 
    
    # part 9 
    def day_name(self):
        """ returns a string that indicates the name of the day of the week 
            of the date object that calls it
        """
        day_names = ['Monday', 'Tuesday', 'Wednesday', 
             'Thursday', 'Friday', 'Saturday', 'Sunday']
        other = Date(11, 9, 2020)
        num_between = self.days_between(other)
        if num_between % 7 == 0:
            return day_names[0]
        elif num_between % 7 == 1:
            return day_names[1]
        elif num_between % 7 == 2:
            return day_names[2]
        elif num_between % 7 == 3:
            return day_names[3]
        elif num_between % 7 == 4:
            return day_names[4]
        elif num_between % 7 == 5:
            return day_names[5]
        else:
            return day_names[6]
        
    
            
            
            

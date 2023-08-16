#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# TT Securities    
#
# Computer Science 111
#

import math

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Find the average of the prices')
    print('(4) Find the standard deviation of the prices')
    print('(5) Find the day of the maximum price')
    print('(6) Find whether or not a price is lower than the threshold')
    print('(7) Find the best buy day, sell day, and resulting profit')
    

    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.
# option 3
def avg_price(prices):
    """ computes and returns the average price of the values given in the input list
        input prices is a list of 1 or more prices
    """
    average = 0
    count = 0
    sum_num = 0
    for x in prices:
        count += 1
        sum_num += x
        average = sum_num / count
    return average

# option 4
def std_dev(prices):
    """ computes and returns the standard deviation of the prices
        input prices is a list of 1 or more prices
    """
    result = 0
    for x in prices:
        diff = x - avg_price(prices)
        diff = diff ** 2
        result = result + diff
    result = result / len(prices)
    return math.sqrt(result)

# option 5
def max_day(prices):
    """ computes and returns the day of the maximum price
        input prices is a list of 1 or more prices
    """
    max_value = 0
    for i in range(len(prices)):
        if prices[i] > prices[max_value]:
            max_value = i
    return max_value

# option 6
def any_lower(prices, value):
    """ returns True if any of the prices are below the threshold
        retruns False if otherwise 
        input prices is a list of 1 or more prices
        input value is an integer threshold
    """
    result = False
    for x in prices:
        if x < value:
            result = True
    return result

# option 7
def find_tts(prices):
    """ computes the best buy day, sell day, and resulting profit of the prices
        input prices is a list of 2 or more prices
    """
    highest = max_day(prices)
    if highest != 0:
        sell_day = highest
        for i in range(highest):
            maxdiff = highest - prices[0]
            if highest - prices[i] > maxdiff:
                maxdiff = highest - prices[i]
                buy_day = i
            else:
                buy_day = 0
    else:
        maxdiff = abs(prices[2] - prices[1])
        for i in range(1, len(prices)):
            for j in range(2, len(prices)):
                d = abs(prices[j] - prices[i])
                if d > maxdiff:
                    maxdiff = d
                    buy_day = i
                    sell_day = j
    resulting_profit = prices[sell_day] - prices[buy_day]
    return [buy_day, sell_day, resulting_profit]
        
    
    
    
def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            avg = avg_price(prices)
            print('The average price is', avg)
        elif choice == 4:
            deviation = std_dev(prices)
            print('The standard deviation is', deviation)
        elif choice == 5:
            day = max_day(prices)
            print('The max price is', prices[day], 'on day', day)
        elif choice == 6:
            value = int(input('Enter your threshold: '))
            lower = any_lower(prices, value)
            if lower == True:
                print('There is at least one value below', value)
            else:
                print('There are no prices below', value)
        elif choice == 7:
            best_deal = find_tts(prices)
            print('Buy on day', best_deal[0], 'at price', prices[best_deal[0]])
            print('Sell on day', best_deal[1], 'at price', prices[best_deal[1]])
            print('Total profit:', best_deal[2])

            
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')

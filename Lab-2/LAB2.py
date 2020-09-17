# LAB2
#Due Date: 09/18/2020, 11:59PM
"""                                   
### Collaboration Statement:
             
"""

## Section 1

class VendingMachine:
    '''
        Classic Vending Machine Class
    '''

    def __init__(self):

        # Initialize stock & Balance
        self.balance = 0

        # ID : [price , qty]
        self.stock = {
            156 : [ 1.5, 3 ],
            254 : [ 2.0, 3 ],
            384 : [ 2.5, 3 ],
            879 : [ 3.0, 3 ] 
        }
        
    def purchase(self, item, qty=1):
        ''' Attempts to buy something from the machine. '''
        
        # Does the item exist
        if item in self.stock:

            # Is the machine stocked
            if self.isStocked():

                # Is the item in stock
                if self.stock[item][1] > 0:

                    # Enough stock to fulfill purchase
                    if qty <= self.stock[item][1]:

                        total = self.stock[item][0] * qty

                        # Enough balance
                        if total <= self.balance:

                            # Update the qty
                            self.stock[item][1] -= qty

                            # Calc new balance set balance to zero
                            change = self.balance - total
                            self.balance = 0

                            if change > 0:

                                return 'Item dispensed, take your ${} back'.format(change)

                            else:
                                return 'Item dispensed' 

                        else:
                            return 'Please deposit ${}'.format((self.stock[item][0] * qty ) - self.balance)

                    else:
                        return 'Current {} stock: {}, try again'.format(item, self.stock[item][1])

                else: 
                    return 'Item out of stock'

            else:
                return 'Machine out of stock'

        else:
            return 'Invalid item'

    def deposit(self, amount):
        ''' Deposits money into the vending machine. '''

        if self.isStocked():
            self.balance += amount
            return 'Balance: ${}'.format(amount)
        else:
            return 'Machine out of stock. Take your ${} back'.format(amount)

    def restock(self, item, stock):
        ''' Adds stock to the vending machine. '''
        
        # Find the item by id
        if item in self.stock:
            
            # Update the stock
            self.stock[item][1] += stock
            return 'Current item stock: {}'.format(self.stock[item][1])

        else:
            return 'Invalid item'

    def isStocked(self):
        ''' A property method that checks for the stock status. '''
        
        for item in self.stock:
            # An item has nonzero stock, return True

            if self.stock[item][1] > 0:
                return True

        # All items have zero stock
        return False
        
    def getStock(self):
        ''' A property method that gets the current stock status of the machine. '''

        # Return stock
        return self.stock

    def setPrice(self, item, new_price):
        ''' Changes the price of an item in the vending machine '''

        # Make sure the item exists and the price is numerical
        if item in self.stock:

            # Update the items price
            self.stock[item][0] = new_price
            
        else:
            return 'Invalid item'

#################################

## Section 2

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    ## * YOU MAY IMPLEMENT SPECIAL METHODS TO SIMPLIFY LINE METHODS

class Line: 
    ''' 
        >>> line1
        y = 1.825x + 3.775
        
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = 4*line1
        >>> line3
        y = 1.825x + 15.1
        >>> line1==line2
        False
        >>> line3==line2
        True
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> line5==9
        False
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
    '''
    def __init__(self, point1, point2):
        # Convert given objects to useable variables
        self.x1 = point1.x
        self.x2 = point2.x

        self.y1 = point1.y
        self.y2 = point2.y 

    def __repr__(self):
        ''' Returns the standard form of the lines equation when the class is called '''
        
        return 'y = {}x + {}'.format(self.getSlope(), self.getIntercept())

    def getDistance(self):
        ''' Returns the distance given the two init points '''
        
        return round(((self.y2 - self.y1)**2 + (self.x2 - self.x1)**2)**0.5, 3)

    def getSlope(self):
        ''' Return the slope given the init points '''

        return (self.y2 - self.y1)/(self.x2 - self.x1)

    def getIntercept(self):
        ''' Returns the Y-intercept of the line '''

        return round( self.y1 - ( self.getSlope() * self.x1), 3)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
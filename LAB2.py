import random
import math

class Pantry:
    """"
        >>> sara_pantry = Pantry()                
        >>> sara_pantry.stock_pantry('Bread', 2)
        'Pantry Stock for Bread: 2.0'
        >>> sara_pantry.stock_pantry('Cookies', 6) 
        'Pantry Stock for Cookies: 6.0'
        >>> sara_pantry.stock_pantry('Chocolate', 4) 
        'Pantry Stock for Chocolate: 4.0'
        >>> sara_pantry.stock_pantry('Pasta', 3)     
        'Pantry Stock for Pasta: 3.0'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 3.0}
        >>> sara_pantry.get_item('Pasta', 2)     
        'You have 1.0 of Pasta left'
        >>> sara_pantry.get_item('Pasta', 6) 
        'Add Pasta to your shopping list!'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry = Pantry()                    
        >>> ben_pantry.stock_pantry('Cereal', 2)
        'Pantry Stock for Cereal: 2.0'
        >>> ben_pantry.stock_pantry('Noodles', 5) 
        'Pantry Stock for Noodles: 5.0'
        >>> ben_pantry.stock_pantry('Cookies', 9) 
        'Pantry Stock for Cookies: 9.0'
        >>> ben_pantry.stock_pantry('Cookies', 8) 
        'Pantry Stock for Cookies: 17.0'
        >>> ben_pantry.get_item('Pasta', 2)       
        "You don't have Pasta"
        >>> ben_pantry.get_item('Cookies', 2.5) 
        'You have 14.5 of Cookies left'
        >>> sara_pantry.transfer(ben_pantry, 'Cookies')
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Rice')
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
    """

    def __init__(self):
        self.items = {}
    
    def __repr__(self):
        return f'I am a Pantry object, my current stock is {self.items}'

    def stock_pantry(self, item, qty):
        if item in self.items:
            self.items[item] = self.items[item] + float(qty)

        else:
            self.items[item] = float(qty)

        return f"Pantry Stock for {item}: {self.items[item]}"

    def get_item(self, item, qty):
        if item not in self.items:
            return f"You don't have {item}"
        
        elif qty > self.items[item]:
            self.items[item] = 0.0
            return f"Add {item} to your shopping list!"
        
        else:
            self.items[item] = self.items[item] - qty
            return f"You have {self.items[item]} of {item} left"
    
    def transfer(self, other_pantry, item):
        if item in other_pantry.items and other_pantry.items[item] > 0: # checks if the item is available to be transferred
            temp = other_pantry.items[item]
            self.items[item] = self.items[item]+temp
            other_pantry.items[item] = 0.0

class Vendor:

    def __init__(self, name):
        '''
            In this class, self refers to Vendor objects
            
            name: str
            vendor_id: random int in the range (999, 999999)
        '''
        self.name = name
        self.vendor_id = random.randint(999, 999999)
    
    def install(self):
        '''
            Creates and initializes (instantiate) an instance of VendingMachine 
        '''
        return VendingMachine()
    
    def restock(self, machine, item, amount):
        '''
            machine: VendingMachine
            item: int
            amount : int/float

            Call _restock for the given VendingMachine object
        '''
        return machine._restock(item, amount)

class VendingMachine:
    '''
        In this class, self refers to VendingMachine objects

        >>> john_vendor = Vendor('John Doe')
        >>> west_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> john_vendor.restock(west_machine, 215, 9)
        'Invalid item'
        >>> west_machine.isStocked
        True
        >>> john_vendor.restock(west_machine,156, 1)
        'Current item stock: 4'
        >>> west_machine.getStock
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Please deposit $1.5'
        >>> west_machine.purchase(156,2)
        'Please deposit $3.0'
        >>> west_machine.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> west_machine.deposit(3)
        'Balance: $3.0'
        >>> west_machine.purchase(156,3)
        'Please deposit $1.5'
        >>> west_machine.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.deposit(300)
        'Balance: $300.0'
        >>> west_machine.purchase(876)
        'Invalid item'
        >>> west_machine.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> west_machine.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> west_machine.purchase(156,3)
        'Please deposit $4.5'
        >>> west_machine.deposit(4.5)
        'Balance: $4.5'
        >>> west_machine.purchase(156,3)
        'Item dispensed'
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Item out of stock'
        >>> west_machine.deposit(6)
        'Balance: $6.0'
        >>> west_machine.purchase(254,3)
        'Item dispensed'
        >>> west_machine.deposit(9)
        'Balance: $9.0'
        >>> west_machine.purchase(879,3)
        'Item dispensed'
        >>> west_machine.isStocked
        False
        >>> west_machine.deposit(5)
        'Machine out of stock. Take your $5.0 back'
        >>> west_machine.purchase(156,2)
        'Machine out of stock'
        >>> west_machine.purchase(665,2)
        'Invalid item'
        >>> east_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> east_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> east_machine.deposit(10)
        'Balance: $10.0'
        >>> east_machine.cancelTransaction()
        'Take your $10.0 back'
        >>> east_machine.purchase(156)
        'Please deposit $1.5'
        >>> east_machine.cancelTransaction()
        >>> ian_vendor = Vendor('Jayy')
        >>> b_machine = ian_vendor.install()
        >>> ian_vendor.restock(b_machine,156, 11)
        'Current item stock: 14'
        >>> b_machine.getStock
        {156: [1.5, 14], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
    '''

    def __init__(self):
        self.stock = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        self.balance = 0.0

    def purchase(self, item, qty=1):
        if item not in self.stock:
            return "Invalid item"
        
        elif not self.isStocked:
            return "Machine out of stock"
        
        elif self.stock[item][1] == 0:
            return "Item out of stock"
        
        elif self.stock[item][1] < qty:
            return f"Current {item} stock: {self.stock[item][1]}, try again"
        
        elif self.balance < qty*(self.stock[item][0]): # checks if the balance is too low, and by how much
            return f"Please deposit ${qty*(self.stock[item][0])-self.balance}"
        
        elif self.balance > qty*(self.stock[item][0]): # checks if the balance is too high and calculates the required amount of change
            self.stock[item][1] = self.stock[item][1]-qty
            temp = self.balance - (qty*self.stock[item][0])
            self.balance = 0.0
            return f"Item dispensed, take your ${float(temp)} back"

        self.stock[item][1] = self.stock[item][1]-qty # if the previous conditions are not satisfied then no adjustments are needed
        self.balance = 0.0
        return "Item dispensed"

    def deposit(self, amount):
        if self.isStocked: # if the machine is stocked, deposit the given amount
            self.balance += amount
            return f"Balance: ${self.balance}"
        return f"Machine out of stock. Take your ${float(amount)} back"

    def _restock(self, item, stock):
        if item not in self.stock: # if the item is valid, add the specified amount to its current stock
            return "Invalid item"
        self.stock[item][1] = self.stock[item][1]+stock
        return f"Current item stock: {self.stock[item][1]}"
        
    @property
    def isStocked(self):
        for item in self.stock: # if atleast one item has a stock greater than zero, return True
            if self.stock[item][1] > 0:
                return True
        return False
        
    @property
    def getStock(self):
        return self.stock

    def cancelTransaction(self):
        if self.balance != 0.0:
            temp = self.balance
            self.balance = 0.0
            return f"Take your ${float(temp)} back"

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self,other):
        if isinstance(other,Point2D) and self.x == other.x and self.y == other.y:
            return True
        return False

class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
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
        >>> line3 = line1*4
        >>> line3
        y = 1.825x + 15.1
        >>> line1==line2
        False
        >>> line3==line2
        True
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> Point2D(45,3) in line5
        False
        >>> Point2D(34,-204) in line5
        True
        >>> line5==9
        False
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> isinstance(line6.getSlope, float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
        >>> Point2D(9,5) in line7
        True
        >>> Point2D(89,5) in line7
        True
        >>> Point2D(12,8) in line7
        False
        >>> (9,5) in line7
        False
    '''
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.x1 = self.point1.x
        self.x2 = self.point2.x
        self.y1 = self.point1.y
        self.y2 = self.point2.y
        self.getSlope
        self.getInterception
        self.getDistance
    
    @property
    def getDistance(self):
        self.distance = round(math.sqrt(((self.x1 - self.x2)**2) + ((self.y1 - self.y2)**2)), 3)
        return self.distance
    
    @property
    def getSlope(self):
        try:
            self.slope = round((self.y2 - self.y1) / (self.x2 - self.x1), 3)
        except ZeroDivisionError:
            self.slope = float('inf')
        return self.slope

    @property
    def getInterception(self):
        try:
            m = self.slope
            self.interception = round(self.y1 - (m * self.x1), 3)
        except TypeError:
            self.interception = None
        return self.interception

    def __str__(self):
        if self.slope == float('inf'):
            return "Undefined"
        
        elif self.slope == 0:
            return f"y = {self.interception}"
        
        elif self.interception < 0:
            return f"y = {self.slope}x - {abs(self.interception)}" 
        
        elif self.interception == 0:
            return f"y = {self.slope}x"
        
        return f"y = {self.slope}x + {self.interception}"

    def __repr__(self):
        return self.__str__()
    
    def __eq__(self,other): # if other is a Line object and its points are equal to self's points, return True
        if isinstance(other, Line) and self.point1 == other.point1 and self.point2 == other.point2:
            return True
        return False
    
    def __mul__(self,c):
        if isinstance(c,int): # multiplies each point component by the int
            new_point_1 = Point2D(self.point1.x * c, self.point1.y * c)
            new_point_2 = Point2D(self.point2.x * c, self.point2.y * c)
            return Line(new_point_1, new_point_2)
        return None
    
    def __rmul__(other,self): # checks if the
        return self * other
           
    def __contains__(self,point):
        if isinstance(point,Point2D) and self.slope != float('inf'):
            if math.isclose(point.y, (self.slope * point.x) + self.interception):
                return True
        return False

def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace intersection with the name of the function you want to test
    #doctest.run_docstring_examples(Line, globals(), name='LAB2',verbose=True)

if __name__ == "__main__":
    run_tests()
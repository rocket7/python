import math #for sqrt
'''
Object Oriented Programming
Homework Assignment
Problem 1¶
Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/05-Object%20Oriented%20Programming/02-Object%20Oriented%20Programming%20Homework.ipynb
'''
class Line:

    def __init__(self,coor1,coor2):
        self.coor1 = coor1 #( x , y)
        self.coor2 = coor2

    def distance(self):
        #using indexing to unpack tuples
        return math.sqrt(((self.coor2[0] - self.coor1[0])**2) + ((self.coor2[1] - self.coor1[1])**2))

        #using tuple unpacking
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        #return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

        #return map(lambda )
        #return filter(lambda )
        # should return 9.43398113

    def slope(self):
        #return (((self.coor1[0]- self.coor2[0])) / ((self.coor2[1]- self.coor1[1])))
        return (((self.coor2[1]- self.coor1[1])) / ((self.coor2[0]- self.coor1[0])))
        # should return 1.6?

    #__str__

    #__len__


class Cylinder:
# Solve for volume
# V = π * r(sq) * h

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        self.pi = 3.14159

    def volume(self):
        return (self.pi * (self.radius ** 2) * self.height)

    def surface_area(self):
        # Surface Area = 2 * pi * r * h+2 * π * r(sq)
        return (2 * self.pi * self.radius * self.height) + (2 * self.pi * self.radius ** 2)

'''
For this challenge, create a bank account class that has two attributes:
https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/05-Object%20Oriented%20Programming/04-OOP%20Challenge.ipynb

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
'''

class Account:

    def __init__(self,owner="Me",balance=100):
        self.owner = owner
        self.balance = balance


    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"Deposited {amount}, Balance is now {self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print(f"Insufficient funds, current balance {self.balance}")
        else:
            self.balance = self.balance - amount
            print(f"Withdrew {amount}, Remaining Balance is {self.balance}")


if __name__ == '__main__':

    #EXAMPLE OUTPUT
    coordinate1 = (3,2)
    coordinate2 = (8,10)

    li = Line(coordinate1,coordinate2)

    print(li.distance()) # 9.433981132056603
    print(li.slope()) # 1.6


    # EXAMPLE OUTPUT
    c = Cylinder(2,3)
    print(c.volume())
    print(c.surface_area())

    a = Account()
    a.deposit(1)
    a.withdraw(100)
    a.withdraw(2)
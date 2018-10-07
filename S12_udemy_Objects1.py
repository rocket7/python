#
# Object oriented programming combines data and the processes that act on that data into objects (encapsulation) vs Imperitive programing which provides a series of instructions
#
# Object Oriented programming still uses imperitive programming via functions and methods
#
# Everything in PYTHON is an OBJECT
#
# When a Function is Part of a Class it is called a Method
#
# Data Attributes / Variables do Not Exist until Value assigned
#


a = 1
b = 2
print(a + b)
print(a.__add__(b))



class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):  # CONSTRUCTOR
        self.make = make
        self.price = price
        self.on = False


    def switch_on(self):
        self.on = True


# Creates INSTANCE of CLASS
kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)


kenwood.price = 9.99
print(kenwood.price)

# Creates INSTANCE of CLASS
hamilton = Kettle("Hamilton", 7.77)
print(hamilton.make)
print(hamilton.price)

print("Models: {0.make} = {0.price},  {1.make} = {1.price}".format(kenwood,hamilton))

print(hamilton.on)
hamilton.switch_on() # Sets to TRUE
print(hamilton.on)

Kettle.switch_on(kenwood) # TURN SWITCH_ON VIA CLASS ITSELF
print(kenwood.on)

kenwood.power = 1.5
print(kenwood.power)
#print(hamilton.power) # This gives error because data attribute does not exist
# Data Attributes / Variables do Not Exist until Value assigned

# IF NOT DEFINED AT INSTANCE WILL GET FROM CLASS
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

# IF NOT DEFINED AT INSTANCE WILL GET FROM CLASS
print("Switch Kettle CLASS to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print("Switch to kenwood to gas power")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__) # TAKES VALUE FROM CLASS





##############
# OBJECTS - EVERYTHING IN PYTHON IS AN OBJECT
###############
"""
CLASS - Template for creating object
OBJECT - An instance of a ClASS
INSTANTIATE - Create an instance of a CLass
METHOD - A function defined in a class
ATTRIBUTE - a variable bound to an instance of a class

"""




# Use return to return a value
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression
x = lambda a : a + 10
print(x(5))

#All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Note: The self parameter is a reference to the class itself, and is used to access variables that belongs to the class.


# TRY EXCEPT FINALLY
try:
    print("Try")
except:
    print("except")

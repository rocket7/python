#test
hello="Hello"
world="World"
print(hello + world)

myInt = 1
print(myInt)

myFloat = 1.1
print(myFloat)

myString = 'singleQuoteString'
print(myString)

myStringDbl = "doubleQuoteString"
print(myStringDbl)

myStringApos = "Adam's"
print(myStringApos)

one = 1
two = 2
three = one + two
print(three)

a, b = 3, 4
print(a,b)

# Exercise - Learnpython.org
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
# NEED % BEFORE VAR
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# LIST
mylist = [1,2,3]
#ERROR - No Index of 10
#print(mylist[10])
print(mylist[1])
#Index 1 = value of 2

#EXERCISE
numbers = [1,2,3]
strings = ["hello", 'world']
names = ["John", "Eric", "Jessica"]

numbers.append(4)
strings.append("trisolaris")

# write your code here
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
#  %f - Floating point numbers
#  %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

data = ("John", "Doe")
data_decimal = 53.44
formatted_string = "Hello %s %s. Your current balance is "

print(formatted_string % data)
#print(formatted_string "%f."  % (data, data_decimal))

#A tuple is a collection which is ordered and unchangeable (a,b,c)
a = "Hello, World!"
print(a[1])
#Prints H

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

b = "Hello, World!"
print(b[2:5]) # returns llo - first char is 0

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" (without leading or trailing spaces)

a = "Hello, World!"
print(len(a)) # returns 13

a = "Hello, World!"
print(a.upper()) # returns HELLO WORLD

a = "Hello, World!"
print(a.replace("H", "J")) # returns Jello World!

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# INPUT NAME >>
print("Enter your name:")
x = input()
print("Hello, " + x)

# MODULUS - %
divisor = 2
product = divisor % 3
print("Product of 3 modulus 2 = %d" % product)

# EXPONENT - **
exponent = 2
print("Exponent 2 ** 2 = %d" % exponent)

# FLOOR - //
floor = 5.95
print("Floor // = %d" % floor)

# BITWISE OPERATORS
# & AND
x = 4 # NEED WHITESPACE AROUND EQUALS
x = x & 3  # same as &=
print(x)

# | OR
x = 4
x = x | 3 # same as |=
print(x)

# ^ XOR
x = 4
x = x ^ 3 # same as ^=
print(x)

# ZERO RIGHT SHIFT
x = 4
x = x >> 3 # same as >>=
print(x)

# ZERO FILL LEFT SHIFT
x = 4
x = x << 3 # same as <<=
print(x)

#SAME MEMORY LOCATION TO COMPARE OBJECTS
a = 1
b = 2
result = a is b
print("a is b %s " % result)

result = a is not b
print("a is not b %s " % result)

result = a in [1, 2, 3]
print("1 in list [1,2,3] %s " % result)

result = a not in (1, 2, 3)
print("1 not in tuple (1,2,3) %s " % result)

#LIST - Is a collection whose order is ordered and changable
thislist = ["apple","banana","pear"]
print(thislist)

thislist = ["apple","banana","pear"]
thislist[1] = "cherry"
print(thislist[1])
thislist.append("grape")
thislist.insert(4, "pomegranate")
print("The length of this list is.. %d" % len(thislist))
print("Values in list are: ")
for x in thislist:
    print(x)

# LIST METHODS
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

#TUPLE - Ordered and UNCHANGABLE
thistuple = ("apple", "banana", "cherry")
print(thistuple)
# prints: ("apple", "banana", "cherry")
#results in error
#thistuple[1] = "blackcurrant"
# The values will remain the same:


#SETS are UNORDERED and UNINDEXED
thisset = {"apple", "banana", "cherry"}
#add multiple items
thisset.update(["orange", "mango", "grapes"])
print(thisset)
# prints :  {"apple", "banana", "cherry", "orange", "mango", "grapes" }
print("banana" in thisset) #True

# SET METHODS
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that are the intersection of to other sets
# intersection_update()	Removes the items in this set that is not present in other, specified set(s)
# isdisjoint()	Returns whether two sets has a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes the specified element
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others


#DICTONARY - A dictionary is a collection which is unordered, changeable and indexed.
thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
#prints - {
#"brand": "Ford",
#"model": "Mustang",
#"year": 1964
#}

x = thisdict["model"]

x = thisdict.get("model")

print(x) #Mustang
thisdict["year"] = 2018
thisdict["color"] = "red"

# SCOPE
# Python relies on indentation, using whitespace, to define scope in the code.


#IF ELIF ELSE

a = 1
b = 99
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


# WHILE
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

while i < 6:
    print(i)
    if i == 3:
        continue
    i += 1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

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


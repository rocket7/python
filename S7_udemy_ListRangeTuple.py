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
print(thistuple(2))
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


#LISTS
car_list = ["Mclaren P1","Porsche GT2 RS","Bugatti Divo","Nissan GTR","Lexus LFA","Ferrari 250 GTO"]
car_list.append("Koenigsegg Regera")
sorted_car_list = sorted(car_list)
for i in car_list:
    print("Dream cars: " + i)

print(sorted_car_list)
even = [2,4,6,8,0]
odd = [1,3,5,7,9]
numbers = even + odd    #This combines list?
numbers2 = [even, odd]    #This creates 2 lists in numbers2 list
print("Sort does not create/return new sorted object {}".format(numbers.sort()))
#Sort method will sort existing object
numbers.sort()
print(numbers)
sorted_numbers = sorted(numbers) #new object

#DIFFERENT FROM JAVA
if sorted_numbers == sorted(numbers):
    print("The lists are equal")
else:
    print("The lists are NOT equal")


##################
# LIST CHALLENGE - QUIZ 3 - SECTION 7 UNIT 49
flowers = [["rose", "red"],
           ["snapdragon", "white"],
           ["daisy", "white"],
           ["lily", "yellow"]
           ]

second_flowers = flowers

second_flowers[1] = ["lilac", 'purple']

second_flowers[1][1] = 'pink'
print(flowers)
# PRINTS ['rose', 'red']['lilac', 'pink']..


###########################
# RANGE QUIZ 1
numbers = range(13)

new_range = numbers[1::2]
for i in new_range:
    print(i, end=', ')
# PRINTS 1,3,5,7,9,11

###########################
# RANGE QUIZ 2
even = range(0, 20, 2)  # ACTAUL NUMBERS ARE 0-19 in INCREMENTS OF 2
#Go Backwards From 19 to 0
for number in even[::-1]:
    print(number, end=', ')
# PRINTS 18,16,14,12,10,8,6,4,2,0


#Creates Empty List
list1 = []
list2 = list() #contructor

#ALL THE SEQUENCE TYPES BUILT INTO PYTHON ARE ITERABLE
print(list("The lists are equal")) #Creates LIST with each CHAR a member

#WHEN YOU COPY LIST YOU COPY OBJECT REFERENCE SO ANY CHANGE TO EITHER WILL UPDATE BOTH
another_even = even #COPY OBJECT
another_even.sort(reverse=True)
print(even)
#EVEN and ANOTHER_EVEN point to SAME List Object
print("another_even is even - True if objects equal")
print(another_even is even) #returns True if object equal
print("\ranother_even == even - True if contents equal")
print(another_even == even) #returns True contents equal


garage = []
garage.append(["Ferrari","Lamborgini", "Pagini"])
garage.append(["Ducati","Moto Guzzi", "Bimota"])
garage.append(["McLaren","Gumbert", "Ariel"])
garage.append(["KTM","Mono", "Triumph"])
print(garage)

#Print List NOT containing KTM
for vehicle in garage:
    if not "KTM" in vehicle:
        for model in vehicle:
            print(model)


string = "1234567890ABCDEFG"
# for each char in string print
my_iter = iter(string)
print(my_iter) #Retrun string object mem address
print(next(my_iter)) #returns 1
print(next(my_iter)) #returns 2

# https://www.udemy.com/python-the-complete-python-developer-course/learn/v4/t/lecture/3925118?start=0
# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list.

i = 0
for collection in garage:
    new_iterator = iter(collection)
    while i < len(collection):
        print(next(new_iterator))
        i += 1


my_list_range = list(range(10)) # 0 to 10 exclusive of 10
print(my_list_range) #prints 0,1,2,3,4,5,6,7,8,9

# RANGE (begin, end, step)

my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index("e")) #prints 4
print(my_string[4]) #prints eprint(next(new_iterator))


# ASSIGN Several Variables at once
a = b = c = d = 10
print(c) #Prints 10

a,b = 1,2 # RIGHT is evaluated first
print(b)  #prints 2

#TUPLES - Don't always require parens
#TUPLES ARE IMUTABLE AND ALLOW MULTIPLE DATA TYPES
NIN = ("Head like a hole", "NIN", 1994)
#NIN[0] = "a" #results in error as tuples are immutable
print(NIN)

#NIN[0] = "a" #results in error as tuples are immutable
#TypeError: 'tuple' object does not support item assignment

#TUPLES ARE IMMUTABLE - BUT YOU CAN RE_CREATE THEM
tuple1 = "Nirvana", "Smells like team Spirit", 1991 #NOTICE FOR PARENS
#Takes values from original tuple and creates new tuple with same name
tuple1 = tuple1[0], "Smells Like Teen Spirit", tuple1[2]
print(tuple1)
#Prints New Updated Tuple

#UNPACKING TUPLE
title, artist, year = NIN
print(title)
print(artist)
print(year)


##################
#TUPLES QUIZ
products = (('No. 5', 'perfume', 'Chanel'),
            ('Inflallible', 'cosmetic', "L'Oreal"),
            ('Poison', 'perfume', 'Dior'),
            ('Double Wear', 'cosmetic', 'Estee Lauder'),
            ('Wonder Wing', 'cosmetic', 'Rimmel London')
            )
# UNPACK TUPLE
for product in products:
    name, type, company = product
    print(company)



#LISTS CAN BE CHANGED
metallica = ["Master of Puppets", "Metallica", 1984]
metallica[0] = "a" #LISTS ARE NOT IMMUTABLE
print(metallica)









# TRY EXCEPT FINALLY
try:
    print("Try")
except:
    print("except")





#############
# For Loops
#############
number = "123,456,789.00"
cleanedNumber = ""
for char in number:
    if char in '0123456789':
        cleanedNumber += char

for state in ["MA", "HI", "CA", "NY"]:
    print("These are my favorite states: " + state)
    #print("These are my favorite states: {}".format(state))

for i in range(1,13):
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i, j, i*j))

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
length = len(quote)
# Use a for loop and an if statement to print just the capitals in the quote above.
capitals = ""
for i in range(0,length - 1):
    if quote[i].isupper():
        capitals += quote[i]
print("Capital letters: " + capitals)

# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char, end='')


min = 0
max = 100
numDivSeven = ([])
for i in range(min, max):
    if i % 7 == 0:
        numDivSeven.append(i)
print("\r\rThe numbers divisibile by Seven are: {}".format(numDivSeven))

# This solution uses a step value for the range function
for i in range(0, 100, 7):
    print(i)

# Modify this loop to stop when i is exactly divisible by 11
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

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

#Creates Empty List
list1 = []
list2 = list() #contructor

#ALL THE SEQUENCE TYPES BUILT INTO PYTHON ARE ITERABLE
print(list("The lists are equal")) #Creates LIST with each CHAR a member
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

#LISTS CAN BE CHANGED
metallica = ["Master of Puppets", "Metallica", 1984]
metallica[0] = "a" #LISTS ARE NOT IMMUTABLE
print(metallica)







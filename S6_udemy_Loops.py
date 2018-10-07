


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


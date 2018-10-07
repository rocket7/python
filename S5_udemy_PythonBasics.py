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


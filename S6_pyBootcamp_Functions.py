# Pierian Python Bootcamp - Section 6
# Functions
# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/tree/master/03-Methods%20and%20Functions

#CHALLENGES
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spygame(x):
    s = ''
    for item in x:
        if item == 0 or item == 7:
            s += str(item)

    if s == '007':
        return True
    else:
        return False


print(spygame([1,2,4,0,0,7,5]))

print(spygame([1,0,2,4,0,5,7]))

print(spygame([1,7,2,0,4,5,0]))

#CHALLENGES
# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# Prime Numbers are greater than 1 and only divisible by 1 and itself

def prime_func(z):
    primes = []

    num = 2
    while num <= z:
        start = 2
        while start < num:
            if num%start == 0:
                break
            elif start == num - 1:
                primes.append(num)
            start += 1

        num += 1
    return(primes)

print(prime_func(10))



#CHALLENGES
# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter

#
#HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
#For purposes of this exercise, it's ok if your dictionary stops at "E".

alpha = {'a':'  *  \n * * \n*****\n*   *\n*   *','b':'****\n*   *\n**** \n*   *\n**** '}
print(alpha['a'])
print(alpha['b'])
#letter = input("Enter letter: ")


#Challenge Homework
# Write a function that checks whether a number is in a given range (inclusive of high and low)


def num_check(num,low,high):
    if num >= low and num <= high:
        return True
    else:
        return False

print("Is number in range: " + str(num_check(2,1,5)))






#Challenge Homework
#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def upper_lower():
    upper = 0
    lower = 0
    data = input("Please enter string to calculate upper and lower case chars: ")
    for x in data:
        if x.islower():
            lower += 1
        elif x.isupper():
            upper += 1
    print(f"Number of UPPER case characters: {upper}")
    print(f"Number of lower case characters: {lower}")

upper_lower()



#Challenge Homework
#Write a Python function that takes a list and returns a new list with unique elements of the first list.

orig_list = ['a', 1, "hello", 2.2]
new_list = [1,2,3,4,5,6,7,8,9]

def zip_list(orig_list, new_list):
    iterator = zip(new_list, orig_list)
    combined_list = list(iterator)
    #combined_list = zip(new_list, orig_list) # DOESN'T WORK
    #print(combined_list) - Prints Object ID
    return combined_list # returns list of tuples
    # [(1, 'a'), (2, 1), (3, 'hello'), (4, 2.2)]

print(zip_list(orig_list,new_list))



#Challenge Homework
#Write a Python function to multiply all the numbers in a list.

num_list = [1,2,3,4,5,6,7,8,9]
total = 1
def multi_num(number):
    for num in number:
        num *= num
    return num

print(multi_num(num_list))






#Challenge Homework
#Write a Python function that checks whether a passed in string is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.


def palindrome():
    letter = 0
    forward_word = input("Enter word: ")
    backword_word = ''
    count = 1
    while letter < len(forward_word):
        backword_word = backword_word + forward_word[len(forward_word) - count]
        letter += 1
        count += 1
    print(backword_word)
    if backword_word == forward_word:
        print("This is a Palindrome")
    else:
        print("This is not a Palindrome")

palindrome()


#Challenge Homework - Hard
#Write a Python function to check whether a string is pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once
alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
new_set = {}
a = {1,2}
b = {1,2}
new_list = []
new_dict = {}
def pangram(s):
    print(a ^ b) # returns set()
    if a ^ b == None:
        print("hello")
        #for item in s:
        #new_set.add(item)
    #print(alphabet ^ new_set)
    #if alphabet ^ new_set == None:

pangram(b)


# SETS - DOES THIS WORK WITH LISTS TOO?
a = {1,2}
b = {2,3}
print(a | b) # UNION = 1,2,3
print(a - b) #
print(a & b) # = 2
print(a ^ b) # = 1,3


















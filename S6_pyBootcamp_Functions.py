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








#Challenge Homework
#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.







#Challenge Homework
#Write a Python function that takes a list and returns a new list with unique elements of the first list.







#Challenge Homework
#Write a Python function to multiply all the numbers in a list.








#Challenge Homework
#Write a Python function that checks whether a passed in string is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.









#Challenge Homework - Hard
#Write a Python function to check whether a string is pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once
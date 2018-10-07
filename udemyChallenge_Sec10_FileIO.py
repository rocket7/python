# Write a program to append the times tables to our jabberwocky poem
# in sample.txt. We want the tables from 2 to 12 (similar to the output
# from the For loops part 2 lecture in section 6).
#
# The first column of numbers should be right justified. As an example,
# the 2 times table should look like this:
#   1 times 2 is 2
#   2 times 2 is 4
#   3 times 2 is 6
#   4 times 2 is 8
#   5 times 2 is 10
#   6 times 2 is 12
#   7 times 2 is 14
#   8 times 2 is 16
#   9 times 2 is 18
#  10 times 2 is 20
#  11 times 2 is 22
#  12 times 2 is 24
#  --------------------





# FILE MODE OPERATORS
# w+ - Read and Write to file
# r - read only
# a - append
###########################
# read - reads entire file
# readlines - reads line by line
###########################
# Add file= modifier to print() function to write output to file


multiple = 2
test_range = range(0,13)

#
# W I T H / A S - AUTOMATICALLY HANDLES CLOSING OF FILE
#


#
#
#

#with open("testfile.txt", 'a') as file:
 #   for a in range(0,13):
  #      if a < 10:
            #print(" " + str(a) + " times " + str(multiple) + " is " + str(a * multiple))
            #print(" " + str(a) + " times " + str(multiple) + " is " + str(a * multiple), file=file)
        #else:
            #print(str(a) + " times " + str(multiple) + " is " + str(a * multiple))
            #print(str(a) + " times " + str(multiple) + " is " + str(a * multiple), file=file)

# https://docs.python.org/2/library/string.html#formatstrings
# {1:>2} - 2 spaces RIGHT JUSTIFIED
# [start at:end before:interval]
# https://docs.python.org/2.3/whatsnew/section-slices.html
# SOLUTION - HE WANTS ALL MULTIPLICATION TABLES
with open("testfile.txt", "a") as file:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i * j)) # file=file
        print("-" * 20) # file=file



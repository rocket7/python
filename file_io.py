###############
# FILE IO
###############
import os
import subprocess

# jabber = open("C:\\python\\testfile.txt", 'r') #read-only
#jabber = open("/Users/thor/IdeaProjects/python/testfile.txt", 'r')
#jabber = open("testfile.txt", 'r')
#jabber.close()


# FILE MODE OPERATORS
# w+ - Read and Write to file
# r - read only
# a - append
###########################
# read - reads entire file
# readlines - reads line by line
###########################
# Add file= modifier to print() function to write output to file


##################################################
# WITH - TRAPS ERROR SO YOU DON'T NEED TO USE CLOSE()
##################################################
with open('testfile.txt', 'r') as jabber:
    for line in jabber:
        if "jabberwock" in line.lower():
            print(line, end='')

###############################
# PRINTS IN >>REVERSE<< IF NOT USING END=''
###############################
with open('testfile.txt', 'r') as jabber:
    lines = jabber.readlines()
print(lines, end='')

###############################
# PRINTS LINE IN REVERSE RIGHT to LEFT and BOTTOM to TOP USING RANGE
###############################
with open('testfile.txt', 'r') as jabber:
    lines = jabber.read()

# https://docs.python.org/2.3/whatsnew/section-slices.html
for line in lines[::-1]:
    print(line, end='')

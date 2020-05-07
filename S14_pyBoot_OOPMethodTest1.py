'''
Advanced Python Objects Test
https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/14-Advanced%20Python%20Objects%20and%20Data%20Structures/06-Advanced%20Python%20Objects%20Test.ipynb
'''

#Advanced Python Objects Test
#Advanced Numbers
#Problem 1: Convert 1024 to binary and hexadecimal representation
number = 1024
print(f"Convert number to hex (hex(number): {hex(number)}")

#Problem 2: Round 5.23222 to two decimal places



#Advanced Strings
s = 'hello how are you Mary, are you feeling okay?'
#Problem 3: Check if every letter in the string s is lower case
l = list(filter(lambda x:x.isupper(),s))
print(f"Number of Uppercase letters {len(l)}")

#Problem 4: How many times does the letter 'w' show up in the string below?
s2 = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
l = list(filter(lambda x:x.count('w'),s2))
print(f"Number of \'w\' letters {len(l)}")

#Advanced Sets
#Problem 5: Find the elements in set1 that are not in set2:
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
set3_union = set2 | set1 # or set1.union(set2)
print(f"UNION of both sets {set3_union}")

#Problem 6: Find all elements that are in either set:
set3_inter = set2 & set1 # or set1.inter(set2)
print(f"INTERSECTION of both sets {set3_inter}")

#Advanced Dictionaries
#Problem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension.
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# DICT COMPREHENSION
new_dict = {key:  value * 2 for key, value in my_dict.items()}
print(f"New Dictionary Comprehension: {new_dict}")

#Advanced Lists
#Problem 8: Reverse the list below_dict:
list1 = [1,2,3,4]
list1.reverse() #IN PLACE REVERSE
print(f"List1 In Place Reverse with .reverse(): {list1}")
print(f"List1.reverse() does not return a list: {type(list1.reverse())}") #Returns NONE Type
rev_list = list1.reverse()
print(f"List1 Reversed: {rev_list}")

#Problem Sort the list below:
list2 = [3,4,2,5,1]
list2.sort()
print(f"Sorted List: {list2}")

#APPEND(OBJ) - Appends to List
list2.append(6)
print(f"Append() List: {list2}")

#COUNT(OBJ) - Returns count of Object
val = list2.count(6)
print(f"Count(Obj) List: {val}")

new_seq_list = [7,8,9]
#EXTEND(SEQ) - IN PLACE UPDATE - DOES NOT RETURN NEW LIST
list2.extend(new_seq_list)
print(f"Extend(Seq) List: {list2}")

#INDEX(OBJ) - Returns Index of Object
val = list2.index(3)
print(f"Index() List: {val}")

#INSERT(INDEX,OBJ) - Insert Object at Index
list2.insert(3,3)
print(f"Insert(index,object) List: {list2}")

#POP(OBJ) - Removes and returns last object
list2.pop(6)
print(f"Pop(object) List: {list2}")

#REMOVE(OBJ) - Removes Object
list2.remove(3)
print(f"Remove(obj) List: {list2}")

#Compare List1 and List2
#print(f"Compare 2 list objects with CMP() - {cmp(list1,list2}")

#Length of list
print(f"Length of list - len(list) = {len(list2)}")

#MIN of list
print(f"MIN of list - min(list) = {min(list2)}")

#Length of list
print(f"MAX of list - max(list) = {max(list2)}")

#List of SEQ - TUPLE
tup = (9,8,7)
print(f"List of SEQ or TUPLE - list(seq or tuple) = {list(tup)}")




################################################################
#
# Challenge # 1 -
#
# www.pythonchallenge.com
#
################################################################

string = """g fmnc wms bgblr rpylqjyrc gr zw fylb. 
rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

url_string = "http://www.pythonchallenge.com/pc/def/map.html"

# ASCII "a" is 97
# ASCII "z" is 122

# TYPE HINT - INT
#
range_plus_1: int = 123

print("Before: " + string)
string.lower()
#
string3 =""

string = string.lower()

#RANGE DOES NOT INCLUDE LAST ITEM IN RANGE - IT IS RANGE - 1
#
# LOOK AT STRING.MAKETRANS() FUNCTION
#
for i in url_string:
    if ord(i) not in range(ord("a"), range_plus_1):
        string3 += i
    elif i == 'y':
        string3 += "a"
    elif i == 'z':
        string3 += "b"
    else:
        string3 += chr(ord(i)+2)


print("\nString3: " + string3)

################################################################
#
# Challenge # 2 - view-source:http://www.pythonchallenge.com/pc/def/ocr.html
#
# www.pythonchallenge.com
#
# http://www.pythonchallenge.com/pc/def/ocr.html
#
################################################################
dict1 = {}

with open("pychallenge2.txt", "r") as rare_char:

    #print("Rarechar = " + rare_char) # RETURNS IOWRAPPER
    rare_char1 = "equality"

    for line in rare_char: #THIS IS LOOKING AT LINE NOT CHAR BECUASE FILE
        for x in line:
            if x not in dict1:
                dict1[x] = 1
            else:
                temp = dict1.get(x)
                print(temp) # RETURNS
                #MUST USE .GET(x) OR RETURNS {KEY:VAL}

                temp = (int(temp) + 1)
                dict1[x] = temp


#print(dict1) - the whole list
#print(dict1.__dir__())  # DESCRIBES METHODS AVAIL
#print(dict1.items())

for key in dict1:
    print("Dictionary Key : Value Pairs {} : {} ".format(key, str(dict1[key])))


#print("String4 - Rare Chars: " + string4)



################################################################
#
# Challenge # 3 - http://www.pythonchallenge.com/pc/def/equality.html
#
# One small letter, surrounded by <b>EXACTLY</b> three big bodyguards on
# each of its sides. (see page source)
#
# www.pythonchallenge.com
#
# answer: l.html
#           linkedlist.php
#
# URLLIB - import urllib
#
################################################################
import re



seven_char4 = ""
saved = []
with open("pychallenge3.txt", "r") as three_bodyguards:

    for line in three_bodyguards: #USE SEARCH NOT MATCH
        if re.search(r'[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}', line):
            saved.append(re.search(r'[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}', line))

    # for line in three_bodyguards:
    #     for x in line:
    #         if len(seven_char4) < 9:
    #             seven_char4 += x
    #             break
    #         elif re.match(r'[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}', seven_char4):
    #         #elif seven_char4[:1].islower() and seven_char4[1:3].isupper() and seven_char4[4].islower() and seven_char4[4:1].isupper() and seven_char4[1:].islower():
    #             saved.append(seven_char4)
    #             #print(saved)
    #             break
    #         else:
    #             new = seven_char4[1:]
    #             seven_char4 = new
import urllib.request

for g in saved:
    try:
        print(g.group(0))
        sevenChar = (g.group(0)[4])
        #sevenChar = "equality"
        print(urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/{}.html".format(sevenChar)))
    except IOError:
        print("404 Error")

#for x in range(0,10):
#    print(str(saved[x])[-11:-2])
#    print(urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/{}.html".format(str(saved[x])[-11:-2])))

# RE

# test = "ABCdEFG"
# print(test[:3], end="") # PRINTS FIRST 3
# print(test[3], end="") # PRINTS 4th CHAR
# print(test[4:])        # PRINTS LAST 3



########################################################################
#
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
#
# <!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never
# end. 400 times is more than enough. -->
#
# chainsaw.jpg

# 44827
#
#httplib, urllib, requests
########################################################################

import requests

r = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
print(r.content) #returns 44827

for pc4 in range(12345,12346):
    pyurl = urllib.request.Request(url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(pc4))

    try:
        with urllib.request.urlopen(pyurl) as f:

            print("HTTP urllib status: {} and reason: {} and content: {}".format(f.status,f.reason))
    except IOError:
        print("HTTP IO 404 Error")



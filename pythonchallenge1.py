
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
# >>> peak.html

# 66831
#httplib, urllib, requests
########################################################################

import requests

#r = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=")
key = "66831"
EOF = True
while EOF == False:
    try:
        r = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + key)
        # NEED TO STRIP OUT NON-NUMERIC CHARS
        if r.status_code == 200:
            k = re.search(r'[0-9].*', str(r.content)[-6:-1])
            print(k.group(0))
            key = str(k.group(0))
            #key = str(int(k) / 2)

            print("Status Code: {} Response Content: {}".format(r.status_code, r.content))
            #input()
        else:
            EOF = True
            break
    except IOError:
        print("HTTP IO 404 Error")


    #pyurl = urllib.request.Request(url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(pc4))


####################################################
# CHALLENGE 5
# http://www.pythonchallenge.com/pc/def/peak.html
# peak.html
#
#Picture of Hill or Peak with Quote - Pronounce It!
#
# Peak hell sounds familiar ? (pickle)
# view-source:http://www.pythonchallenge.com/pc/def/banner.p
#
# python3 -m pickletools banner.p
####################################################

import pickle # object serialization - load everything in memory
import pprint

import array
peak_str = ""
peak_array = []
peak_2array = [[],[]]
peak_dict = {}
x = 0

# with open("banner.p", "r") as peak:
#     for row in peak:
#         with open("banner_dump.p", "wb") as pickle_line:
#             pickle.dump(row, pickle_line, -1)
#         #peak_array.append(row)

#with open("banner_dump.p","rb") as pickle_file:
with open("pychallenge5.txt","rb") as pickle_file:
    try:
        d = pickle.load(pickle_file)
        pprint.pprint(d)
        print(d)
        #pickle.load(pickle_file, fix_imports=True)
    except EOFError:
        print(EOFError)

print("*"*25)

for row in d:
    #print(row)
    for item in row:
        temp = str(item[0])*item[1]
        print(temp, end='')
    print("\n")

# LOADS REQUIRES BYTES OBJECT
# with open("banner2.p","rb") as pickle_file:
#     data = pickle_file.read()
#     pickle.loads(data, encoding="ASCII")

#         pickle.loads(pickle_file)
#
#         pickle.loads(pickle_file, encoding="ASCII")
#
#     except IOError:
#         pass

#
# with open("pychallenge5.txt", "r") as peak:
#      for row in peak:
#         if len(peak_dict) == 0:
#             peak_dict[row] = 1
#         elif row in peak_dict:
#             peak_dict[row] = peak_dict[row] + 1
#         else:
#             peak_dict[row] = 1
#
# for key, value in sorted(peak_dict.items()):
#     print("Key: {} Value: {}".format(key, value))

         #
         # if peak_array[].count() > 0:
         #     while x < peak_array[].count():
         #        if row == peak_array[x]val:
         #     peak_array[[val]]++
         #     break
         # else:
         #     peak_array[].append(row)
         #
         #     peak_dict.items()
         # elif peak_dict.get(row) == False:
         #     peak_dict.items()


data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

output = open('banner2.p', 'wb')
# Pickle dictionary using protocol 0 - DEFAULT
pickle.dump(data1, output)
output.close()

with open("banner2.p", "rb") as ff:
    #ff = output.read()
    l = pickle.load(ff)
    pprint.pprint(l)
    ff.close()

print("************************************************")
test = ["aaa"]
test2 = [["aaa", 1],["bbb", 2]]
test3 = [["aaa"],["bbb"]]
print(test[0]) # Prints 1
print(test2[1][1]) # Prints 2
print(test3[1]) # Prints 2
print("Length of test2: " + str(len(test2)))

########################################################################################
#
# Challenge 6
# http://www.pythonchallenge.com/pc/def/channel.html
# <!-- <-- Zip -->
# Now there are pairs
#
# https://docs.python.org/3.5/library/functions.html#zip
# Zips iterables into tuple pairs
# channel.zip
########################################################################################

#import zip #FUNCTION

s1 = "<!-- <-- zip -->"
s2 = "now there are pairs"
s3 = "channel"
a = zip(s1,s2) #Zips ITERABLE List

print("*"*25)
#
# hint 1 - start from 90052
# answer is inside the zip
import zipfile

zip_list = []
zfile = "channel.zip"
file = '90052' # 46145.txt - collect the comments.
file_ext = '.txt'
print(file + 'aaa\nbbb' + file_ext)
x = 0

#zf = zipfile.ZipFile(zfile, mode="r")
#comments = []
comments = ""
with zipfile.ZipFile(zfile, "r") as myzip:
    zlist = myzip.infolist()
    print(len(zlist))
    #print(myzip.comment) #ZipFile COmment
    #print(myzip.infolist)
    while x < 909:
        #comments.append(str(myzip.getinfo(file + file_ext).comment)[2:-1])
        comments += str(myzip.getinfo(file + file_ext).comment)[2:-1]
        try:
            with myzip.open(file + file_ext, 'r') as f:
                next =f.read()
                #comments.append(myzip.getinfo(f))
                #zi = zipfile.ZipInfo(file + file_ext)
                #comments.append(str(zi.comment(f))) # comments.append(myzip.getinfo(f))
                #print(f.comment)
                file = str(next[16:])[2:-1]
                x += 1
                print(x)
                if file == 46145:
                    break
        except KeyError:
            print(KeyError)

#PRINT COMMENTS ON ZIPFILE
myzip.close()
#print(comments, end='\n')  # PRINTS WHOLE LINE AND NOT CARRIAGE RETURN
for char in comments:
    if char == '\\':
        print('', end='\n')
    elif char == 'n':
        print('', end='')
    else:
        print(char, end='')




# with zipfile.ZipInfo(zfile,"r") as myzip:
#     #myzip.comment
#     print(myzip.comment)
#     myzip.close()

################################################################################
#
# hockey.html
# http://www.pythonchallenge.com/pc/def/oxygen.html
# Challenge 7
# Displays Greyscale Bar and Title of "smarty"
# view-source:http://www.pythonchallenge.com/pc/def/oxygen.png
# view-source:http://www.pythonchallenge.com/pc/def/oxygen.html
#
################################################################################
from PIL import Image #cannot have PIL and pillow

import requests
from io import BytesIO
from PIL import Image


img = Image.open('oxygen.png')
#exif_data = img.getexif()
#print("Exif data =".format(exif_data))

print("width " + str(img.width))
print("height {}".format(img.height))
print("getpixels {}".format(img.getpixel((0,47))))






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

width = img.width
height = img.height
block_size = 0
center = height / 2
rgb_array = []
tuple = ()

print("width " + str(img.width))
print("height {}".format(img.height))
#print("getpixels {}".format(img.getpixel((0,47))))
for x in range(0,width):
    print("{} RGB : {}".format(x,img.getpixel((x,center))))
    if len(rgb_array) == 0:
        rgb_array.append(img.getpixel((x,center)))
    elif rgb_array[len(rgb_array) - 1] == img.getpixel((x,center)):
        continue
    else:
        rgb_array.append(img.getpixel((x,center)))

for z in rgb_array:
    print(chr(z[0]),end='')
print("\n")
print(chr(105),chr(110),chr(116),chr(101),chr(103),chr(114),chr(105),chr(116),chr(121))

# flaw in program skip if number repeats - like 1

#i n t e g r i t y


#####################################################################
# CHALLENGE #8
# http://www.pythonchallenge.com/pc/def/integrity.html
# view-source:http://www.pythonchallenge.com/pc/def/integrity.html
# notinsect
# shape = poly
# title = working hard
######################################################################

print("*" * 20)
print("Challenge #8")
print("*" * 20)

import hashlib
import bz2

import PIL.ImageDraw as ImageDraw
import PIL.Image as Image

un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw ='BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

image2 = Image.open("integrity.jpg", "r")

coords="179,284,214,311,255,320,281,226,319,224,363,309,339,222,371,225,411,229,404,242,415,252,428,233,428,214,394,207,383,205,390,195,423,192,439,193,442,209,440,215,450,221,457,226,469,202,475,187,494,188,494,169,498,147,491,121,477,136,481,96,471,94,458,98,444,91,420,87,405,92,391,88,376,82,350,79,330,82,314,85,305,90,299,96,290,103,276,110,262,114,225,123,212,125,185,133,138,144,118,160,97,168,87,176,110,180,145,176,153,176,150,182,137,190,126,194,121,198,126,203,151,205,160,195,168,217,169,234,170,260,174,282"

draw = ImageDraw.Draw(image2)
coords_list = coords.split(',')
print(coords_list[0])
count = 0
coord_list2 = []
temp = ''
for c in coords_list:
    if count == 0:
        temp = c
    elif count % 2 != 0:
        coord_list2.append((int(temp),int(c)))
        #print(coord_list2)
    else:
        temp = c
    count += 1

#DRAW AND DISPLAY IMAGE
#points = (coord_list2)
#draw.polygon((points), fill=200)
#image2.show()

import hashlib
import base64
import bz2

#test_string = "this is a string"
#out = ""
#output_hash = base64.encodebytes(b"donkey")
#print(f"base64 - donkey {output_hash}")

#output_hash = base64.encodebytes(b"This is a Horse")
#print(f"base64 - horse {output_hash}")

#sha1 = hashlib.sha1()
#sha1.update(b"This is a Horse")
#print(sha1.digest())

#with open("pychal8_bzip.bz2",mode="r") as file:

bzip2file = "pychal8_bzip.bz2"

f = bz2.open(bzip2file) #BZ2File binary file

#with open(bzip2file, 'rb') as file:

#file = open(bzip2file, mode='rb')
print("Result of bzip un bytes string decompress: " + str(bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')))
#huge
print("Result of bzip pw bytes string decompress: " + str(bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')))
#file

#with bz2.open("pychal8_bzip.bz2",mode="r") as bzf:
#    bzf.decompress()



#####################################################################
# CHALLENGE #9 - connect the dots
# http://www.pythonchallenge.com/pc/return/good.html
# view-source:http://www.pythonchallenge.com/pc/return/good.html
#
#
#
######################################################################

print("*" * 20)
print("Challenge #9")
print("*" * 20)


image9 = Image.open("good.jpg", "r")

coords1="146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,\
310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,\
190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,\
389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,\
215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,\
290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,\
279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,\
327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,\
328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,\
259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,\
352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,\
120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,\
214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,\
102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,\
113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,\
133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,\
111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,\
332,155,348,156,353,153,366,149,379,147,394,146,399"

coords2="156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159,\
157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220,\
125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,\
77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,\
158,121,157,128,156,134,157,136,156,136"

draw = ImageDraw.Draw(image9)
coords_list1 = coords1.split(',')
coords_list2 = coords2.split(',')
#print(coords_list[0])
count = 0
coord_list1 = []
coord_list2 = []
temp = ''
for c in coords_list1:
    if count == 0:
        temp = c
    elif count % 2 != 0:
        coord_list1.append((int(temp),int(c)))
        #print(coord_list2)
    else:
        temp = c
    count += 1

count = 0
for c in coords_list2:
    if count == 0:
        temp = c
    elif count % 2 != 0:
        coord_list2.append((int(temp),int(c)))
        #print(coord_list2)
    else:
        temp = c
    count += 1

#DRAW AND DISPLAY IMAGE
#points = (coord_list1)
#draw.polygon((points), fill=100)
#points = (coord_list2)
#draw.polygon((points), fill=200)
#image9.show()

#bull


#####################################################################
# CHALLENGE #10 - connect the dots
# http://www.pythonchallenge.com/pc/return/bull.html
# a = [1, 11, 21, 1211, 111221,
# len(a[30]) = ?
# what are you looking at? (bull)
# view-source:http://www.pythonchallenge.com/pc/return/bull.html
# coords = "146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,332,155,348,156,353,153,366,149,379,147,394,146,399"
#
######################################################################

print("*" * 20)
print("Challenge #10")
print("*" * 20)

coords = "146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,332,155,348,156,353,153,366,149,379,147,394,146,399"
coords10 = coords.split(',')
count = 0
coord_list10 = []
temp = ''
for c in coords10:
    if count == 0:
        temp = c
    elif count % 2 != 0:
        coord_list10.append((int(temp),int(c)))
        #print(coord_list2)
    else:
        temp = c
    count += 1

#DRAW AND DISPLAY IMAGE
points = (coord_list10)
draw.polygon((points), fill=100)
image9.show()


# https://www.answers.com/Q/What_row_of_numbers_comes_next_1_11_21_1211_111221_312211_13112221
#def count_num_positions():
input_string = "11" #input("Please enter INTEGER to start evaluation...")
length = 0
index_position = 0


# ALGORITHM
# 11 = 21 ( 2 1's)

# ARRAY
calculated_string_array= []

calculated_string_array[0]= input_string

#Add First Entry
calculated_string_array.append(input_string)
print(f"Print value of calculated_string_array: {calculated_string_array[0]}")

count = 0
#while len(calculated_string_array) <= 31:
#for count in range(0,31):
for x in range(0,len(calculated_string_array)):
    if calculated_string_array[0][0] == calculated_string_array[z][x]:
        #ERROR
        print(f"same - {calculated_string_array[0][0]} - {calculated_string_array[][x]}")
        if x == len(calculated_string_array[0]) - 1:
            val = str(x + 1) + calculated_string_array[0]
            calculated_string_array.append(val)
            break
            #print(f"calculated_string_array = {calculated_string_array}")
    else:
        val = str(x + 1) + calculated_string_array[0]
        calculated_string_array.append(val)
        print(f"calculated_string_array = {calculated_string_array[0]}")
    #for x in calculated_string_array[count]:
        #print(f"Print value of x: {x}")
        #calculated_string_array = x

    #length = len(input_string)
    #index_position = input_string.count()
    #if index_position < length:



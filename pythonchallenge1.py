#pythonchallenge

string = """g fmnc wms bgblr rpylqjyrc gr zw fylb. 
rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
sqgle qrpgle. kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

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
for i in string:
    if ord(i) not in range(ord("a"), range_plus_1):
        string3 += i
    elif i == 'y':
        string3 += "a"
    elif i == 'z':
        string3 += "b"
    else:
        string3 += chr(ord(i)+2)


print("\nString3: " + string3)
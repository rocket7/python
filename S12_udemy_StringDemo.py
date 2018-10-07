a_string = "this is\na string split\t\tand tabbed"
print(a_string)

#---------> \/
raw_string = r"this is\na string split\t\tand tabbed"
print(raw_string)

#CHR(10) LINE FEED
#CHR(13) Carriage return (windows)
b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

backslash_string = "this is a backslash \followed by some text"
print(backslash_string)

backslash_string = "this is a backslash \\followed by some text"
print(backslash_string)

error_string = r"this string ends with \\"
print(error_string)

extended_ascii = "ASCII Extended " + chr(246)
print(extended_ascii)
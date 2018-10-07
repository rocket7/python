#!/usr/bin/env python

def python_food():
    print("spam and eggs")

#ALL FUNCTIONS RETURN A RESULT - if NOthing Specified it returns NONE
print(python_food())


def center_text(*args, sep=' ', end='\n', file=None, flush=False): #PARAMETER
    text = ""
    for arg in args:
        text += str(arg) + sep
    #text = str(text)  #NUMBERS DON'T HAVE A LENGTH
    left_margin = (80 - len(text) // 2)
    print(" " * left_margin, text, end=end, file=file, flush=flush)
    return " " * left_margin + text


# with open("centered.txt", mode='w') as centered_file:
#
#     # CALL FUNCTIONS
#     s1 = center_text("spam and eggs", file=centered_file) #ARGUMENT
#     print(s1)
#     center_text("spam, spam and eggs", file=centered_file)
#     center_text("spam, spam, spam and eggs", file=centered_file)
#     center_text(123) #NUMBERS DON'T HAVE A CHAR LENGTH
#
#     # CTRL CLICK TO SEE OBJECT DETAILS - IE PRINT()
#
#     center_text("first", 1, "Second", 2, sep=" : ", file=centered_file) # Automatically adds spaces
#
#     # JOIN() ONLY WORKS WITH STRINGS


# CALL FUNCTIONS
center_text("spam and eggs")#ARGUMENT
center_text("spam, spam and eggs")
center_text("spam, spam, spam and eggs")
center_text(123) #NUMBERS DON'T HAVE A CHAR LENGTH

# CTRL CLICK TO SEE OBJECT DETAILS - IE PRINT()

center_text("first", 1, "Second", 2, sep=" : ") # Automatically adds spaces

print("=" + str(12 * 3))
print(sorted(["b", "c", "a", "d"]))

# # JOIN() ONLY WORKS WITH STRINGS

with open("output/menu.txt", "w") as menu:
    s1 = center_text("spam and eggs")
    print(s1, file=menu)
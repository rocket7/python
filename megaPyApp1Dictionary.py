'''
mega python course on udemy
application#1
load json dictionary and prompt user for word to look up and present defntion
'''

import json
import difflib
import mysql.connector
from difflib import SequenceMatcher
from difflib import get_close_matches

json_dictionary = "megaPyApp1Dictionary.json"
prompt = "Please enter dictionary word to lookup in dictionary: "
db_or_json = "JSON"
con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

# class lookup(object):
def match_word(word, data):
    matches = get_close_matches(word, data.keys(), cutoff=0.85)
    matches.append(get_close_matches(word.title(), data.keys(), cutoff=0.85))
    matches.append(get_close_matches(word.upper(), data.keys(), cutoff=0.85))
    if len(matches) == 1:
        matches = get_close_matches(word, data.keys())[0]  # Gets only top match - array zero
        print(f"There was no direct match for {word}, however the following word is a close match: {matches}")
        prompt = input(f"Would you like to use this {matches[0]} instead [y|n]?")
        if prompt == 'y':
            print(f"The definition for word {matches[0]} is: {data.get(matches[0])}")
        else:
            print(f"The word {word} was not found in dictionary")
    elif len(matches) > 1:
        print(f"There was no direct match for {word}, however the following words are a close match: {matches}")
        for x in matches:
            print(f"{matches.index(x)} : {x}")
        prompt = input(f"Would you like to use one of these words instead [y|n]?")
        if prompt == 'y':
            selection = int(input(f"Enter number of word to use instead?"))
            # print(f"matches = {type(matches)}") #list
            # print(f"matches[0] = {matches[0]}")
            # print(f"selection = {type(selection)}") #int
            print(f"The definition for word {matches[selection]} is: {data.get(matches[selection])}")
        else:
            print(f"The word {word} was not found in dictionary")
    else:
        print(f"There were no similar words found in dictionary")


class lookup:

    def __init__(self, dictionary):
        self.word = None
        self.matches = []
        self.dictionary = dictionary

    def definition(self, word):
        # JSON LOAD TAKES FILE OBJECT - MUST USE OPEN - HELP(JSON.LOAD)
        with open(self.dictionary) as file:
            data = json.load(file)
            # print(type(data)) #dict
            if data.get(word):  ## if word in data:
                print(f"The definition for word {word} is: {data[word]}")
            elif data.get(word.title()):  ## if word.title() in data:
                print(f"The definition for word {word.title()} is: {data[word.title()]}")
            elif data.get(word.upper()):  ## if word.upper() in data:
                print(f"The definition for word {word.upper()} is: {data[word.upper()]}")
            else:
                match_word(word, data)


##ISSUE IF SEARCHING FOR Pariss - only looks for lowercase

if __name__ == '__main__':
    if db_or_json == "JSON":
        l = lookup(json_dictionary)  # create lookup object
        i = str.lower(input("Please enter word to search for in dictionary: "))
        l.definition(i)
    elif db_or_json == "DB":
        cursor = con.cursor()

        query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'line'")
        results = cursor.fetchall()

        for result in results:
            print(result[1]) #second item in tuple

    else:
        print("Invalid db_or_json value selected")

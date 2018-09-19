###############
# DICTIONARY
###############

#A DIctionary is a set of Key / Value pairs

fruit = {"orange": "A sweet, citrus fruit from FL or CA", "banana": "A yellow curved fruit that is high in potassium"}

print(fruit["banana"]) # prints value associated with [key] banana

# You CAN ADD to a Dictionary by specifying a new KEY and giving a value
fruit["blueberry"] = "A delicious small blue berry"
print(fruit) #prints everything including braces

#Invalid Key
print(fruit["invalid key"]) #returns error

fruit.clear()
print(fruit)

# Asks for key and prints description
while True:
    dict_key = input("Please enter fruit: ")
    if dict_key == "q":
        break
    description = fruit.get(dict_key) #does not give error if not existing
    print(description)

# DICTIONARY KEY MUST BE IMMUTABLE
bike = {"make": "Honda", "model": "250 dream", "colour": "red", "engine_size": 250}
print(bike["engine_size"])
print(bike["colour"])

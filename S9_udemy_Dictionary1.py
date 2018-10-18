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
#print(fruit["invalid key"]) #returns error

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

# https://docs.python.org/2.3/whatsnew/section-slices.html
print("{1:>2} aaa".format(1,2,3)) # PRINTS 2
print("{1:>2} aaa".format(2,1,3)) # PRINTS 1
print("{1:>2} aaa".format(10,1,3)) # PRINTS 1

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")


# POWER OF PROPERTY vs GETTER AND SETTER

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)

# LOOK AT CLASS DEFINITION FOR PROPERTY
# https://www.programiz.com/python-programming/property
#The last line of the code, makes a property object temperature.
# Simply put, property attaches some code (get_temperature and set_temperature) to the member attribute accesses (temperature).

#Any code that retrieves the value of temperature will automatically call get_temperature() instead of a dictionary (__dict__) look-up.
#Similarly, any code that assigns a value to temperature will automatically call set_temperature(). This is one cool feature in Python.

man = Celsius()
man.temperature = 37
man.temperature  #37
#Whenever we assign or retrieve any object attribute like temperature, as show above, Python searches it in the object's __dict__ dictionary.
#
#>>> man.__dict__
#{'temperature': 37}
#Therefore, man.temperature internally becomes man.__dict__['temperature'].
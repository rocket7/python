########################
# WRITE TO FILE
########################

#A DIctionary is a set of Key / Value pairs
# DICTIONARY KEY IS IMMUTABLE
# DICTIONARY KEY MUST BE IMMUTABLE
bike = {"make": "Honda", "model": "dream", "colour": "red", "engine_size": 250}
print(bike["engine_size"])
print(bike["colour"])

###############
# SETS - IMMUTABLE, UNORDERED AND CONTAINS NO DUPLICATES
###############
animals = {"dog", "cat", "lion", "elephant", "tiger", "kangaroo"}
print(animals)

# WITH DICTIONARY IT IS USING KEY NOT VALUE
# WRITES TO FILE
with open("output.txt", 'w') as file1:
    for a in bike:
        print(bike[a], file=file1) # CANNOT HAVE SPACES AROUND EQUALS FOR ARGUMENTS

with open("output.txt", 'r') as bike_file:
    contents = bike_file.readline()

print(contents) # Honda


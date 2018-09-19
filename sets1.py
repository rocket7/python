###############
# SETS - UNORDERED AND CONTAINS NO DUPLICATES
###############

# MUST BE IMMUTABLE

# CAN USE UNION AND INTERSECTION OPERATIONS

# CAN BE USED TO CLEAN UP DATA

animals = {"dog", "cat", "lion", "elephant", "tiger", "kangaroo"}
print(animals)

birds = set(["eagle", "falcon", "pigeon", "bluejay", "flamingo"])
print(birds)

for animal in birds:
    print(animal)

birds.add("woodpecker")
animals.add("woodpecker")

print(animals)
print(birds)

class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

a = 12
b = 1
print(a + b)
print(a.__add__(b))

kenwood = Kettle("Kenwood", 8.99)
print(kenwood.price)
print(kenwood.make)

kenwood.price = 9.99
print(kenwood.price)


##############
# OBJECTS
###############

# EVERYTHING IN PYTHON IS AN OBJECT






import pickle # object serialization - load everything in memory

# PICKLE OBJECT SERIALIZATION
# https://docs.python.org/3/library/pickle.html
# STORE OBJECTS TO A FILE WITH OBJECT DATA
# PICKLE WRITES AS BINARY FILE

#TUPLE - IS FIRST ONE ZERO?
imelda = ("More Mayhem",
          "Imelda May",
          "2011",
          ((1, "Pulling the rug"),
           (2, "Psycho"),
           (3, "Mayhem"),
           (4, "Kentish Town Waltz")))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)
    pickle.dump(1234567, pickle_file)


with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)

#print(imelda2)

album, artist, year, track = imelda2

print(album)
print(artist)
print(year)
print(track)  # ((1, 'Pulling the rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz'))

print('*' * 20) # prints 20 astericks

for i in range(0, 4):  # WHY DOES THIS DO 1 - 4??  AND NOT 0 - 3?
    print(track[i])

for a in even_list:
    print(a)

print(x)


# with open("binary", 'bw') as bin_file:
#     bin_file.write(bytes(range(17)))
#
# with open("binary", 'br') as binFile:
#     for b in binFile:
#         print(b)


a = 65534       # FF FE
b = 65535       # FF FF
c = 65536       # 00 01 00 00
x = 2998302     # 02 2D C0 1E

with open("binary2", 'bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'little'))

with open("binary2", 'br') as bin_file:
    e = int.from_bytes(bin_file.read(2), 'big')
    print(e)
    f = int.from_bytes(bin_file.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_file.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_file.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_file.read(4), 'big')
    print(i)







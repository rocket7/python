from S12_udemy_GetSet_Player import Player
#import S12_udemy_GetSet_Player

from S12_udemy_Inherit_Enemy import Enemy, Troll, Vampire, VampireKing

tim = Player("Tim", 1, 1000)

#Accessing Values Directly
print(tim.name)
print(tim.lives)

tim._set_lives(10)
print(tim._get_lives)
print(tim)

tim.lives -= 1
print(tim.lives)
print(tim)

tim.lives += 5
print(tim.lives)
print(tim)

tim.lives -= 2
print(tim.lives)
print(tim)

#tim.lives = 9
#print(tim)

#
#  Python does not need getters and setters unlike c and java
#
#  Can sometimes be useful to do some error checking
#
#  Python Uses PROPERTIES instead
#

tim.lvl = 5
#print(tim.lvl)
print(tim)

tim.lvl = -2
#print(tim.lvl)
print(tim)

tim.lvl = 3
#print(tim.lvl)
print(tim)

tim.lvl = -20
#print(tim.lvl)
print(tim)

# DOES NOT KEEP NEGATIVE NUMBER
# EVALUATING RIGHT TO LEFT
# NEGATIVE - MINUS NEGATIVE = POSITIVE
tim.level -= -10
print(tim)




###############################
#
# INHERITANCE - UDEMY - Section 12 - Unit 132 0 SUb-Classes
#
###############################
print("\n\n\nINHERITANCE")


random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

# ONE Args
ugly_troll = Troll("test troll")
print("Ugly troll - {}".format(ugly_troll))

# # Three Args - DOES NOT MATCH CONSTRUCTOR
# another_troll = Troll("Another Troll Set Superclass",1000,1)
# print("Another troll - {}".format(another_troll))
#
#
# #Two Args - DOES NOT MATCH CONSTRUCTOR
# big_troll = Troll("Another Troll Set Superclass",1000)
# print("Big troll - {}".format(big_troll))

ugly_troll.grunt()

# PYTHON DOESN'T HAVE OVERLOADED METHODS - CAN GET SAME EFFECT WITH NAMED PARAMS AND DEFAULTS
# PYTHON ONLY HAS ONE CONSTRUCTOR


# ONE Args
count_dracula = Vampire("Count Dracula")
print("Count Dracula - {}".format(count_dracula))

count_dracula.take_damage(14)
print(count_dracula)

while count_dracula.alive:
    if not count_dracula.dodge_attack():
        count_dracula.take_damage(1)
        print(count_dracula)


# ONE Args
king_vlad = VampireKing("King Vlad")
print("King Vlad - {}".format(king_vlad))

king_vlad.take_damage(14)
print(king_vlad)

while king_vlad.alive:
    if not king_vlad.dodge_attack():
        king_vlad.take_damage(10)
        print(king_vlad)

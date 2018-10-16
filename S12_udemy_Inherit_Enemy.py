# Base class for Game Application
#class Enemy(object) - Python 3

import random

class Enemy:

    def __init__(self, name, hit_points, lives):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("Player took {} points of damage and has {} points remaining".format(damage, self.hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.alive = False


    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit Points: {0.hit_points}".format(self)

#
#SUBCLASS OF ENEMY
#
class Troll(Enemy):
    #pass

    def __init__(self, name):
        #CALLING SUPERCLASS INIT METHOD - PYTHON2 - Enemy.__init__(self, name=name, hit_points=0, lives=1)

        #super(Troll, self).__init__( name=name, hit_points=0, lives=1)
        super().__init__( name=name, hit_points=23, lives=1)

    def grunt(self):
        print("Me {0.name}, stomp you".format(self))

#
#SUBCLASS OF ENEMY
#
# 3 lives and 12 hit points
class Vampire(Enemy):
    #pass


    def __init__(self, name):
        #CALLING SUPERCLASS INIT METHOD - PYTHON2 - Enemy.__init__(self, name=name, hit_points=0, lives=1)

        #super(Troll, self).__init__( name=name, hit_points=0, lives=1)
        super().__init__( name=name, hit_points=12, lives=3)

    def suck_blood(self):
        print("Vampire {0.name}, wants to suck your blood".format(self))


    #OVERRIDES SUPERCLASS METHOD - NOT OVERLOADED AS THIS IS NOT SUPPORTED
    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("Player took {} points of damage and has {} points remaining".format(damage, self.hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.alive = False


    def dodge_attack(self):

        if random.randint(1,3) == 3:
            print("***** {0.name} dodged attack *****".format(self))
            return True
        else:
            return False

#
#SUBCLASS OF VAMPIRE
#
# 3 lives and 12 hit points
class VampireKing(Vampire):
    #pass


    def __init__(self, name):
        #CALLING SUPERCLASS INIT METHOD - PYTHON2 - Enemy.__init__(self, name=name, hit_points=0, lives=1)
        #CALLING VAMPIRE NOT ENEMY SO NEED TO INITIALIZE NEW VARIABLES
        # INIT METHODS WILL CALL UP CHAIN TO PARENT
        super().__init__(name) # INIT FOR VAMPIRE CLASS - WILL CALL INIT FOR ENEMY CLASS
        self.hit_points = 140

    def suck_blood(self):
        print("VampireKing {0.name}, wants to suck your blood".format(self))


    #OVERRIDES SUPERCLASS METHOD - NOT OVERLOADED AS THIS IS NOT SUPPORTED
    def take_damage(self, damage):
        super().take_damage(damage // 4) #INTEGER DIVISION DAMAGE BY 4
        # HOLD CMD KEY (MAC) TO SEE PARENT CLASS OF OBJECT - ie: take_damage






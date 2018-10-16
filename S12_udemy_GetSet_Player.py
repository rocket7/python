class Player(object):

    def __init__(self, name, level=1, score=1000):
        self.name = name
        self._lives = 10  # _ Hidden Indicator for data attribute that shouldn't be called directly
        self.level = level
        self._score = score


    def _get_lives(self):
        return self._lives


    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("lives cannot be negative")


    def get_level(self):
        return self.level


    def set_level(self, lvl):
        print("Current level: {}".format(self.level))
        print("Current lvl: {}".format(lvl))
        if lvl > 0:
            self.level_up(lvl)
        elif self.level - lvl >= 1:
            self.level_down(lvl)
        else:
            print("Level cannot be set below 1")



    def level_up(self, lvl):
        self.level += lvl
        self._score += (lvl * 1000)

    # DOES NOT KEEP NEGATIVE NUMBER
    # EVALUATING RIGHT TO LEFT
    # NEGATIVE - MINUS is POSITIVE

    def level_down(self, lvl):
        self.level = self.level + lvl
        self._score = self._score + (lvl * 1000)


    @property
    def score(self, score):
        return self._score


    @score.setter
    def score(self, score):
        self.score = score

#
# Data Attribute Cannot have same NAME as Property - ie: Lives
#
    lives = property(_get_lives, _set_lives)

#### SHOULD NOT BE NAMED SAME AS INSTANCE VARIABLE
###DO NOT WANT METHOD NAMES IN PROPERTY
    lvl = property(get_level, set_level)

# String Replacement FIeld
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0._score}".format(self)


# Challenge - Section 12 - Unit 129 - Udemy
# -----------------------------------------
# Modify the PLAYER class so player scores are increased by 1000 every time level increased by 1
#
# If Player Drops a Level they will lose 1000 for each level
#
# Cannot go below level 1

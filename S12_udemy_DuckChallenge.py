class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Wee, this is fun")
        elif self.ratio == 1:
            print("this is hard work but I am flying")
        else:
            print("I think that I'll just walk")




class Duck(object):
# WHEN A CLASS CONTAINS ANOTHER OBJECT IT'S CALLED COMPOSITION
    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")


    def swim(self):
        print("Come on in, the water's lovely")


    def quack(self):
        print("Quack quack")


    def fly(self):
        self._wing.fly()



class Penguin(object):

    def __init__(self):
        self.fly = self.aviate()

    def walk(self):
        print("Waddle, waddle, penguids waddle too")


    def swim(self):
        print("Come on in, the water's chilly this far south")


    def quack(self):
        print("Are you havin' a laugh - I'm a penguin")

    def aviate(self):
        print("I won the lottery and bought a lear jet")


class mallard(Duck):
    pass


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


class Mallard(Duck):
    pass

class Flock(object):

    def __init__(self):
        self.flock = []
        #EMPTY LIST

    def add_duck(self, duck: Duck) -> None:  #PARAM ANNOTATION WITH COLON TYPE AND RETURN VALUE
        #if type(duck) is Duck:  #BAD PRACTICE
        #Use ISINSTANCE Instead
        fly_method = getattr(duck, 'fly', None) #Checks Attribue DIsctionary to CHeck if Data Attribute Exists
        #if isinstance(duck, Duck):
        if callable(fly_method):
            self.flock.append(duck)
            #ADD NEW DUCK TO FLOCK
        else:
            raise TypeError("Cannot add duck, are you sure it's not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("Testing exception in migrate") # TODO remove before release
            except AttributeError as e:
                problem = e
                if problem:
                    raise #Error up call stack

            #MAKE DUCKS FLY




if __name__ == '__main__':
    donald_duck = Duck()
    test_duck(donald_duck)
    print("*" * 24)
    donald_duck.fly()
    print("*" * 24)
    percy = Penguin()
    test_duck(percy)





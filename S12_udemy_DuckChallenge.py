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

    def walk(self):
        print("Waddle, waddle, penguids waddle too")


    def swim(self):
        print("Come on in, the water's chilly this far south")


    def quack(self):
        print("Are you havin' a laugh - I'm a penguin")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == '__main__':
    donald_duck = Duck()
    test_duck(donald_duck)
    print("*" * 24)
    donald_duck.fly()
    print("*" * 24)
    percy = Penguin()
    test_duck(percy)
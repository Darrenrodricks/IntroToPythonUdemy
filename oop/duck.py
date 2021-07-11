class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Wee, this is fun")
        elif self.ratio == 1:
            print("this is hard work, but I am flying")
        else:
            print("I think i'll just walk")


class Duck(object):

    def __init__(self):
        self._winghtml = Wing(1.8)

    def walk(self):
        print("Waddle, Waddle, Waddle")

    def swim(self):
        print("Come on in, the water is lovely")

    def quack(self):
        print("Quack Quack")

    def fly(self):
        self._wing.fly()

class Penguin(object):

    def walk(self):
        print("Waddle, Waddle, I waddle too")

    def swim(self):
        print("come on in, its a bit chilly though")

    def quack(self):
        print("are you 'ayin' a larf? I'm a penguin")

# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == '__main__':
    donald = Duck()
    donald.fly()


    # percy = Penguin()
    # test_duck(percy)

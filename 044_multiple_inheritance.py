# multiple inheritance = when a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("This animal flees")

class Preditor:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hwak(Preditor):
    pass

class Fish(Prey, Preditor):
    pass

rabbit = Rabbit()
hwak = Hwak()
fish = Fish()

rabbit.flee()
hwak.hunt()
fish.hunt()
fish.flee()
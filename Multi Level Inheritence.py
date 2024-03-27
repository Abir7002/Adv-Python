class SuperHero:
    def avenger(self):
        print("This is a Avengers")

class IronMan (SuperHero):
    def iron(self):
        print("This is a Iron Man")

class Child (IronMan):
    def chid(self):
        print("This is a Child")

avs = Child()
avs.chid()
avs.iron()
avs.avenger()

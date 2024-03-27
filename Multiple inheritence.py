class Cartoon:
    def tom(self):
        print("This is a Tom")

class Jerry:
    def jer(self):
        print("This is a Jerry")

class dog(Cartoon,Jerry):
    pass

car = dog()
car.jer()
car.tom()


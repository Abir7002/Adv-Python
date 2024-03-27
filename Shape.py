class shape:
    def set(self,a):
        self.x=a
    print("This is a set function")

class Rec(shape):
    def show(self):
        print(self.x)




R1 = Rec()

R1.set(10)
R1.show()


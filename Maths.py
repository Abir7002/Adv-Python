class add:
    def sum(self,a,b):
        print(a+b)
class multiply:
    def mul(self,a,b):
        print(a*b)
class subtract(add,multiply):
    def sub(self,a,b):
        print(a-b)
math = subtract()
math.sum(4,5)
math.mul(5,6)
math.sub(10,5)

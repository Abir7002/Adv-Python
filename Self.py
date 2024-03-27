class Abir:
    a = 10

    def sqrt(self):
        print(f"Square of innner variable is {self.a**2}")

    def __init__(self,x):
        self.a = x
        print(f"Square of inner variable through init is {self.a**2},type of data is {type (self)}")

    def __del__(self):
        print("Data will destroy")

new = Abir(2)

new.sqrt()
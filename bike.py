class Bike:
    def __init__(self,model,color,price):
        self.model = model
        self.color = color
        self.price = price

    def mybike(self):
        print(self.model,self.color,self.price)

b1 = Bike("Glamer","Red",100000)
b2 = Bike("fz","Blue",30000)
b1.mybike()
b2.mybike()


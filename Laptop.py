class Laptop:
    def price(Self):
        return 40000

class Dell(Laptop):
    def price(self):
        return 50000

class Lenovo(Laptop):
    def price(self):
        return 60000

class Asus(Laptop):
    def price(self):
        return 100000

i3 = Dell()
i5 = Lenovo()
i7 = Asus()

print("The Dell i3 price is ",i3.price(),"Rs")
print("The Lenovo i5 price is ",i5.price(),"Rs")
print("The Asus i7 price is ",i7.price(),"Rs")

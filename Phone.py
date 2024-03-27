class Mobile:
    def price(self):
        return 1000
class Vivo(Mobile):
    def price(self):
        return 10000

class Poco(Mobile):
    def price(self):
        return 20000
class Iphone(Mobile):
    def price(self):
        return 80000

v3 = Vivo()
m4pro = Poco()
proMax = Iphone()

print("This Vivo Phone Price is :",v3.price(),"Rs")
print("This Poco Phone Price is :",m4pro.price(),"Rs")
print("This Iphone Phonr Price is :",proMax.price(),"Rs")

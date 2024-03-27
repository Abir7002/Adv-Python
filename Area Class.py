class Shape:

     def rec(self):
         l = int(input("Enter the lenth number :"))
         b = int(input("Enter the breth number :"))
         self.area = l*b
         print(self.area)

     def cir(self):
         r = int(input("Enter the Radius of circle :"))
         self.area = 3.14*r**2
         print(self.area)

     def menu(self):
        print("Press the button 1 to show the Area of Rectrangle")
        print("Press the button 2 to show the Area of Circle")
        self.a = int(input("Input your Option"))
        if self.a == 1:
            self.rec()
        elif self.a == 2:
            self.cir()
        else :
            print("Kuch nhi hai ")

x = Shape()
x.menu()






# x = Shape()
# x.rec()
#
# y = Shape()
# y.cir()



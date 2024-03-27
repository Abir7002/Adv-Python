# class home :
#     def show(self):
#         self.a = "Hello World"
#         print(self.a)
#
#
# x = home()
#
#
# x.show()
#
# y = x.show
#
# y()



def f(self,x,y):
    return max(x,y)

class c:
    a = f
    def g(self):
        return "Hello World"
    h = g

x = c()

print(x.h())
print(x.a(15,24))

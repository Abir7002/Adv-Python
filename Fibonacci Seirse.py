a = 0
b = 1
t = int(input("Enter the number you want"))
c = 0

def fab(a,b,t,c):
    if t == 0:
        return 0
    else:
        print(a)
        c = a+b
        a = b
        b = c
        fab(a,b,t-1,c)

fab(a,b,t,c)


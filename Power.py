x =int(input("Enter A Base Number"))
y =int(input("Enter A power Number"))
t = x

def power(x,y):
    if(y==1):
        return x
    else:
        x *= power(x,y-1)
        return x

print(f"power of base {t} with power {y}is{power(t,y)}")

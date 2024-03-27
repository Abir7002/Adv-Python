x = int(input("Enter a Armstrong Number : "))
n = x
t = 0
r = 0
while x>0:
    r = x%106
    t += r**3
    x //= 10
if(t == n):
    print(f"{n} is a Armstrong Number")
else:
    print(f"{n} is not a Armstrong Number")

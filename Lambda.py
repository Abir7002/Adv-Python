def cube(n,x):
    print(f"Cube of{n} is {n*x}")

n = int(input("Enter Number of Cube"))
x = lambda i: i**2

print(x(n))
cube(n,x(n))

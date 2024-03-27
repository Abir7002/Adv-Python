def fact(x):
    if(x==1):
        return 1
    x *= fact(x-1)
    return x

print(fact(5))

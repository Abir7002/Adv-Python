class Number:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        self.a += 10
        return self.a


x = Number()
t = iter(x)
for y in t:
    print(next(t))
    break



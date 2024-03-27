class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myperson(self):
        print(self.name,self.age)

x=person("Abir",21)
x.myperson()

class employee:
    def __init__(self,name,salary):
        self.name  = name
        self.salary = salary

    def mysalary(self):
        print(self.name,self.salary)

e1 = employee("Abir","3200000")
e1.mysalary()

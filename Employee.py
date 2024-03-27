class Employee:
    def Salary(self):
        return 15000

class Manager(Employee):
    def Salary(self):
        return 50000
class Data_Science(Employee):
    def Salary(self):
        return 100000

Abhishek = Employee()
Manish = Manager()
Abir = Data_Science()

print("Salary is ",Abhishek.Salary())
print("Salary is ",Manish.Salary())
print("Salary is ",Abir.Salary())

from datetime import date

class Person:
    def __init__(self,Name,Country,Date_of_Birth):
        self.Name = Name
        self.Country = Country
        self.Date_of_Birth = Date_of_Birth

    def age(self):
        today = date.today()
        age = today.year-self.Date_of_Birth.year
        return age

p1 = Person("Abir","India",date(2003,5,8))
print(p1.Name)
print(p1.Country)
print(p1.Date_of_Birth)
print(p1.age())

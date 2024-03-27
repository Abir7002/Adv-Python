class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*radius**2
    def perimeter(self):
        return 2*3.14*radius
radius = int(input("Enter the radius"))
circle = Circle(radius)
area =circle.area()
perimeter=circle.perimeter()
print("The area is:", area)
print("The perimter is :", perimeter)

class Circle:
    pi = 3.14

    def __init__(self,radius):
        self.radius = radius
    
    def getArea(self):
        return round(self.radius**2 * self.pi)
    
    def getPerimeter(self):
        return round(self.pi*2 * self.radius) 

circy = Circle(4.44)
print(circy.getArea())
print(circy.getPerimeter())

import math
class Circle():
    def __init__(self, radius):
        self.radius=radius
    def getArea(self):
        return self.radius**2*math.pi
    def getPerimeter(self):
        return self.radius*2*math.pi
daire=Circle(4.44)
print(daire.getArea())
print(daire.getPerimeter())
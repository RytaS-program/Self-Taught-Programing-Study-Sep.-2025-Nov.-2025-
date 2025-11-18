#問1
class Apple:
    def __init__(self,w,c,p,h):
        self.weight=w
        self.color=c
        self.place=p
        self.hard=h

#問2
import math

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def caluculate_area(self):
        return self.radius**2*math.pi

a_circle=Circle(4)
print(a_circle.caluculate_area())
        
#問3
class Triangle:
    def __init__(self,w,l):
        self.width=w
        self.lenth=l

    def calculate_area(self):
        return self.width*self.lenth/2

a_triangle=Triangle(5,10)
print(a_triangle.calculate_area())

#問4
class Hexagon:
    def __init__(self,a,b,c,d,e,f):
        self.per1=a
        self.per2=b
        self.per3=c
        self.per4=d
        self.per5=e
        self.per6=f

    def calculate_perimeter(self):
        return self.per1+self.per2+self.per3+self.per4+self.per5+self.per6

perimeter=Hexagon(4,4,4,4,4,4)
print(perimeter.calculate_perimeter())
        


#問1
class Rectangle:
    def __init__(self,w,l):
        self.width=w
        self.len=l

        
    def calculate_premeter(self):
        return self.width*2+self.len*2

class Square:
    def __init__(self, sr):
        self.sround=sr

    def calculate_premeter(self):
        return self.sround*4

a_rectangle=Rectangle(5,10)
print(a_rectangle.calculate_premeter())

a_square=Square(5)
print(a_square.calculate_premeter())

#問2
class Square:
    def __init__(self, s1):
        self.s1=s1

    def calculate_premeter(self):
        return self.s1*4

    def change_size(self,new_size):
        self.s1+=new_size

a_square=Square(100)
print(a_square.s1)

a_square.change_size(200)
print(a_square.s1)

#問3
class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self,width,length):
        self.width=width
        self.length=length

    def calculate_premeter(self):
        return self.width*2+self.length*2

class Square(Shape):
    def __init__(self,s1):
        self.s1=s1

    def calculate_premeter(self):
        return self.s1*4

a_rectangle=Rectangle(20,20)
a_square=Square(10)

a_rectangle.what_am_i()
a_square.what_am_i()
print(a_rectangle.calculate_premeter())
print(a_square.calculate_premeter())
        
#問4
class Horse:
    def __init__(self,name, breed, owner):
        self.name=name
        self.breed=breed
        self.owner=owner

class Rider:
    def __init__(self,name):
        self.name=name

take=Rider("Take Yutaka")
deep=Horse("Deep Impact", "Competition Horse",take)
print(deep.owner.name)


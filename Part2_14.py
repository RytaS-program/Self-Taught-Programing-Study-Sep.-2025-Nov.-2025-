#問1
class Square:
    square_list=[]

    def __init__(self,s1):
        self.s1=s1
        self.square_list.append((self.s1))

    def calculate_perimeter(self):
        return self.s1*4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square")

a_square=Square(10)
print(Square.square_list)
another_square=Square(20)
print(Square.square_list)

#問2
class Square:
    def __init__(self,s1):
        self.s1=s1

    def __repr__(self):
        return"{} by {} by {} by {}".format(self.s1,self.s1,self.s1,self.s1,)

r1=Square(29)
print(r1)


#問3
class Oasis:
    def __init__(self):
        self.name='Liam'

liam=Oasis()
liam_gallagher=liam
print(liam is liam_gallagher)

liam_buchanan=Oasis()
print(liam is liam_buchanan)

def compare(obj1,obj2):
    return obj1 is obj2

print(compare("a","b"))


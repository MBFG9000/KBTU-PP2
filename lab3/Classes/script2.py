class Shape:
    "new class called Shape that has 0 area by default"
    def __init__(self):
        self._area = 0
    def area(self):
        print(self._area)

class Square(Shape):
    "subclass of the Shape class that take lenght as a argument in init func"
    def init(self , lenght):
        self.lenght=lenght
        self._area=lenght**2

class Rectangle(Shape):
    "subclass of the Shape class that size func that take w and l as a arg"
    def __init__(self,l,w):
        self.lenght=l
        self.width=w
        self._area=l*w
""" few test things here """
a=Square()
a.init(3)
a.area()
print(Square.__doc__)

b=Rectangle(3,4)

b.area()
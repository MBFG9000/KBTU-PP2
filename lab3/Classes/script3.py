import math

class Point:
    "this class make point and you can calculate dist move it and show"
    def __init__(self,x:int=0,y:int=0):
        self.x=x
        self.y=y
    def show(self):
        print (f"Your point is on this coordinate ({self.x},{self.y})")
    def move(self):
            print(f"Your point is on this coordinate ({self.x},{self.y})")
            coorlist=input("Type new coordinates here like-> x y :\t").split()
            self.x,self.y = int(coorlist[0]),int(coorlist[1])
    def dist(self,x0=0,y0=0):
        distance = math.sqrt(pow((self.x-x0),2)+pow((self.y-y0),2))
        print(distance)


a=Point()
a.move()
a.dist(3,4)
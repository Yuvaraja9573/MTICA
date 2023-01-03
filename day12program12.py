class Rectangle:
    def __init__(self,length,width):
        assert(length>=0 and width>=0),'INVALID'
        self.length=length
        self.width=width
    def calculateArea(self):
        return self.length*self.width
    def calculateperimeter(self):
        return 2*(self.length+self.width)
l=int(input())
w=int(input())


try:
    ob=Rectangle(l,w)
    area=ob.calculateArea()
    peri=ob.calculateperimeter()
    print("Area of rectangle is",area)
    print("perimeter of Rectangle is",peri)
except AssertionError as ob:
    print(ob)

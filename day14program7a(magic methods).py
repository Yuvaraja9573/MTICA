#Magic Methods (or) "dunders"
#are special methods which have leading and trailing double underscore
#usee for operator overloading
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __add__(self,ob):
        temp=self.real+ob.real,ob.real+ob.img
        return temp
    def __str__(self):
        return(self.real,self.img)
ob1=Complex(3,5)
ob2=Complex(2,1)
ob3=ob1+ob2
print(ob3)

#class attribute is shared by all instance of the class
#class attribute can be accessed either
#from instance of the class, or the class
class Dog:
    price=400
    def __init__(self,name,color): 
        self.color=color
        self.name=name
    def bark(self):
        print("Woof")
        print(self.name, "has ",self.price,
              "price and its color is ", self.color)
if __name__=="__main__":
    pet1=Dog("Tommy","brown")
    pet2=Dog("Lucky","white")
    pet1.bark()
    pet2.bark()
    print(pet1.price)
    print(pet2.price)
    print(Dog.price)
    Dog('abc','blue').bark()

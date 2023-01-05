#inheritance is a way to share functionality between classes.
class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
#cat and dog are subclasses
class Cat(Animal):
    def mew(self):
        print("Cat meows")
class Dog(Animal):
    def bark(self):
        print("Woof")
if __name__=="__main__":
    print(__name__)
    pet1=Dog("tommy","brown")
    pet2=Cat("lucky","white")
    pet1.bark()
    pet2.mew()
    print(pet1.name,pet1.color)
    print(pet2.name,pet2.color)
    

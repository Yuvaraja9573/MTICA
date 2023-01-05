#Indirect inheritance or mutltilevel inheritance.
class A:
    def first_method(self):
        print("Method of class A...")
class B:
    def first_method(self):
        print("Method of class B...")
class C(A,B):#B,A
    def third_method(self):
        print("Method of class C...")
if __name__=='__main__':
    ob=C()
    ob.first_method()
    ob.third_method()
    #c().third_method()
#circular inheritance is not possible.

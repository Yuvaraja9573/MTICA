class Number:
    def __init__(self,n):
        self.n=n
    def calculateFactorial(self):
        if self.n==0:
            return 1
        res=1
        for i in range(1,self.n+1):
            res*=i
        return res
    def checkEvenOdd(self):
       if self.n%2==0:
            return "Even"
       else:
            return "Odd"
    def sumofDigits(self):
        if self.n<0:
            self.n=abs(self.n)
        temp=str(self.n)
        t=0
        for i in temp:
            t+=int(i)
        return t
    def Armstrong(self):
        str1=str(self.n)
        total=0
        for i in str1:
            total+=int(i)**len(str1)
        if inp==total:
            return 1
        else:
            return 0
       
    
inp=int(input())
obj=Number(inp)
print('Factorial of ',inp,'is',obj.calculateFactorial())
print(inp ,"is",obj.checkEvenOdd())
print("sum of Digits of",inp,'is',obj.sumofDigits())
print("Armstrong of",inp,'is',obj.Armstrong())

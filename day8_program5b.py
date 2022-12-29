def checkEven(num1):
    if num1%2==0:
        return "Even"
    return None


def checkodd(num1):
    if num1%2==1:
        return "odd"
    return None

num=int(input("Enter a no:"))
x=checkEven(num)
y=checkodd(num)

print("x=",x)
print("y=",y)

print(checkEven(num))
print(checkodd(num))

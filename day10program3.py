def fun(str1):
    print(str1)
    return
fun("I'm first call to user defined function!")
fun("Again second call to the same function")

def printme(str1,n):
    n[0]='yuvaraj'
    print(str1,n)
    return
x=['raj','murali']
printme("wakeup",x)
print('x:',x)

def changeme(lstn):
    lstn=['parveen','uma','yuvaraj']
    print(lstn)
    return
lst=[1,4,11,55]
print(changeme(lst))
print('lst:',lst)

##def printpattern(n):
##    num=1
##    for i in range(1,n+1):
##       print(i*'*')
##inp=int(input())
##printpattern(inp)
##



##def printpattern(s,n):
##    assert(n>=0),'INVALID'
##    for i in range(n):
##        print(s*i)
##s=input()
##n=int(input())
##try:
##    printpattern(s,n)
##except AssertionError as a:
##    print(a)

'''reverse pattern'''
def printpattern(s,n):
    assert(n>=0),'INVALID'
    for i in range(n,0,-1):
        print(s*i)
s=input()
n=int(input())
try:
    printpattern(s,n)
except AssertionError as a:
    print(a)
       


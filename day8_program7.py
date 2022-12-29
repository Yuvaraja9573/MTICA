def printSeriesIncreasing(ch,n):
    for i in range(1,n+1,1):
        print(ch*i)
    return None
def printSeriesDecreasing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
    return None

inpch=input("Enter a character:")
inpnum=int(input("Enter a no:"))
printSeriesIncreasing(inpch,inpnum)
print('-'*40)
printSeriesDecreasing(inpch,inpnum)

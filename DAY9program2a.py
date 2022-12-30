def printSeries(n):
    
    for i in range(1,n+1):
        print()
        for j in range(i):
            print(n,end=' ')
            
    return None

inpNum=int(input())
printSeries(inpNum)

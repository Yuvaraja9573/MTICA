def printseries( n):
    if n<0:
        print('invalid')
    else:
        for i in range (1,n+1):
            num=1
            print()
            for j in range(i):
                print(num,end='')
                num+=1
                
    
inpNum=int(input())
printseries(inpNum)

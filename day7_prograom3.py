#for all the number 100-110,use a nested
#list/dictionary comprehension to find the highest
#singe digit any of the numbers is divisible by

ans=[]
for i in range(100,111):
    temp=[]
    for j in range(1,10):
        if i%j==0:
            temp.append(j)
    ans.append([i,max(temp)])
print(ans)



###method-2

##ans=[]
##for i in range(100,111):
##    ans.append([i,max([ j for j in range(1,10)if i%j==0])])
##print(ans)


       
###method-3

##ans=[[i,max([ j for j in range(1,10)if i%j==0 ])] for i in range(100,111)]
##print(ans)





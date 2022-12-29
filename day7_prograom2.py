#nasted list comprehension
#find all numbers 1-100 to divisible by 2 to 9

ans=[]
for i in range(1,101):
    if i%2==0 or i%3==0 or i%4==0 or i%5==0 or i%6==0 or i%7==0 or i%8==0 or i%9==0:
        ans.append(i)
print(*ans)



###method-2

##ans=[]
##for i in range(1,101):
##    for j in range(2,10):
##        if i%j==0:
##            ans.append(i)
##            break
##print(ans)



###method-1.1


##ans=[i for i in range(1,101)  if i%2==0 or i%3==0 or i%4==0 or i%5==0 or i%6==0 or i%7==0 or i%8==0 or i%9==0  ]
##print(ans)


#method-2.1

##ans={i for i in range(1,101)for j in range(2,10)if i%j==0}
##print(ans)


#use list comprehension to contruct a new list but add 6 to each item.

lst=[10,15,20,25,30,35,40,45]
ans=[]
for i in lst:
    ans.append(i+6)
print(ans)




#method-2

##ans=[(i+6) for i in lst]
##print(ans)



##squares
##ans=[(i*i) for i in lst]
##print(ans)

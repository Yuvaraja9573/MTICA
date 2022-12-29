#use list comprehension,contruct a list from the squares of each element in the list,if the square is greater than 50.


lst=[10,15,20,25,30,35,40,4]
ans=[]
for i in lst:
    if i*i>50:
        ans.append(i*i)
print(ans)




#method-2


##ans=[i*i for i in lst if i*i>50]
##print(ans)

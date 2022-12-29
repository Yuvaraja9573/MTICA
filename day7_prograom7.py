#use list comprehension,contruct a new list but squares root of each element in the list.



lst=[10,15,20,25,30,35,40,45]
ans=[]
for i in lst:
    ans.append(round(i**0.5,4))
print(ans)






#method-2

##ans=[(round(i**0.5,4))for i in lst]
##print(ans)

#remove empty strings
lst=["seden","suv","","","pickup",'',' ']

ans=[]
for i in lst:
    if i:
        ans.append(i)
print(ans)





#method-2


##ans=[i for i in lst if i]
##print(ans)

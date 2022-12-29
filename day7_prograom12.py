nums=[11,22,33,44,55]


import math
print(nums)
result=[]
for i in nums:
    result.append(math.sqrt(i))
print(result)




#method-1

##result=[math.sqrt(i)for i in nums]
##print(result)



#mathod-2

##result=list(map(math.sqrt,nums))#name of funtion, iterator
##print(result)

def result(s1,s2):
    return[int(i)+int(j)for i,j in zip(s1,s2)]
inp1=input().strip().split()
inp2=input().strip().split()
print(*result(inp1,inp2))



##def reverse(s1,s2):
##  return[i[::-1]for i,j in zip(s1,s2)]
##inp1=input().strip().split()
##inp2=input().strip().split()
##print(*reverse(inp1,inp2))

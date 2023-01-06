a=input().split()
b=input().split()
c=[]
for i,j in zip(a,b):
    c.append(int(i)+int(j))
print(*c)

    

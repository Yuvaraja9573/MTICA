'''{'Ten':10, 'Twenty':20, 'Thirty':30}'''



keys=['Ten', 'Twenty', 'Thirty']
values=[10,20,30]
d=dict()
for i,j in zip(keys,values):
    d[i]=j
print(d)

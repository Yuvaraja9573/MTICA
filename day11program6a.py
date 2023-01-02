sample_dict={
    "name": "raju",
    "age": 22,
    "salary":80000,
    "city":"New york"}
##  keys to remove
keys=["name", "salary"]

d=dict()
for i in sample_dict.keys()-keys:
   d[i]=sample_dict[i]
print(d)

fo1=open(r"D:\pythonpractice66\DAY10\program7.txt","r")
fo2=open(r"D:\pythonpractice66\DAY10\pg8a.txt","w+")

temp=fo1.read()
fo2.write(temp)

fo1.close()
fo2.close()
print("file copied")    

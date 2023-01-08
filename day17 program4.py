import sys
print("coming through stdout")
save_stdout=sys.stdout
fh=open(r"D:\pythonpractice66\DAY17\Test1.txt","w")
sys.stdout=fh
print("This line goes to test.txt")
print(input())
sys.stdout=save_stdout
fh.close()

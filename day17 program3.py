import sys
#it's easy to print this list:
print(sys.argv)
#or it can be iterated via a for loop:
for i in range(len(sys.argv)):
    if i==0:
        print("Function name:{0}".format(sys.argv[0]))
        #print("Function name:%s"%sys.argv[0])
    else:
        print("{0}.argument:{1}".format(i,sys.argv[i]))
        

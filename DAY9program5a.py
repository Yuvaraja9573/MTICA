def printMonth(dn):
    if(dn==1):
        mn='January'
    if(dn==2):
        mn='February'
    if(dn==3):
        mn='March'
    if(dn==4):
        mn='April'
    if(dn==5):
        mn='May'
    if(dn==6):
        mn=='June'
    if(dn==7):
        mn=='July'
    if(dn==8):
        mn=='August'
    if(dn==9):
        mn=='September'
    if(dn==10):
        mn=='october'
    if(dn==11):
        mn=='November'
    if(dn==12):
        mn=='December'

    return mn
        
def printMonth1(dn):
    if(dn==1):
        mn='January'
    elif(dn==2):
        mn='February'
    elif(dn==3):
        mn='March'
    elif(dn==4):
        mn='April'
    elif(dn==5):
        mn='May'
    elif(dn==6):
        mn=='June'
    elif(dn==7):
        mn=='July'
    elif(dn==8):
        mn=='August'
    elif(dn==9):
        mn=='September'
    elif(dn==10):
        mn=='october'
    elif(dn==11):
        mn=='November'
    elif(dn==12):
        mn=='December'
    else:
        return "invalid"
    return mn
    
import time
for i in range (3):
    inpNum=int(input())
    start=time.time()
    print(printMonth(inpNum))
    print((time.time()-start)*100000000)
    start=time.time()
    print(printMonth1(inpNum))
    print((time.time()-start)*100000000)                              





    

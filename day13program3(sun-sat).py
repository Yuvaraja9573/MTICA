def printsunday():
    print("sunday")
def printmonday():
    print("monday")
def printtuesday():
    print("tuesday")
def printwednesday():
    print("wednesday")
def printthursday():
    print("thursday")
def printfriday():
    print("friday")
def printsaturday():
    print("saturday")
def choose():
    print("enter day no between 1 to 7")
dayDict={1:printsunday,2:printmonday,3:printtuesday,4:printwednesday,5:printthursday,6:printfriday,7:printsaturday}
choose()
dayNo=int(input())
if dayNo>=1 and (dayNo<=7):
    dayDict[dayNo]()
else:
     print("invalid")


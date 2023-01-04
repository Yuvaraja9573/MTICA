def printBlue():
    print('you choose blue!\n')
    return
def printRed():
    print('you choose red!\n')
def printOrange():
    print('you choose orange!\n')
def printYellow():
    print('you choose yellow!\n')
def choice():
    print("0:Blue")
    print("1:Red")
    print("2:Orange")
    print("3:Yellow")
    print("4:Quit")
    return
ColorSelect={0:printBlue,1:printRed,2:printOrange,3:printYellow}
selection=0
while True:
    if selection==4:break
            choice()    
    selection=int(input("selection a color option:"))
    if(selection>=0)and(selection<4):
        ColorSelect[selection]()

def CheckEvenOdd(num1):
    assert(num>0),"Negative Numbers"
    if num1%2==0:
        return"Even"
    else:
        return"Odd"




for i in range(3):
    num=int(input("Enter a no:"))
    try:
        print(num,"is",CheckEvenOdd(num))
    except AssertionError as ob:
        print(ob)

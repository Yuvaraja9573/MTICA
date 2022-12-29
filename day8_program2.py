def Fact(n):
    assert (isinstance(n,int)),"Factorial not defined for non integer"
    assert (n >=0),"Factorial of negattive number is not defined"
    if n==0:
        return 1
    else:
        return n*Fact(n-1)
try:
    print(Fact(3))
except Exception as ob:
    print(ob)
try:
    print(Fact(-3))
except Exception as ob:
    print(ob)
try:
    print(Fact(3.8))
except Exception as ob:
    print(ob)
try:
    print(Fact('today'))
except Exception as ob:
    print(ob)

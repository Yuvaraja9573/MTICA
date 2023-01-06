'''make a function inside a function,
which uses the variables x as a non local variables:'''

def myfunc1():
    x="Raju"
    def myfun2():
        nonlocal x
        x="hello"
    myfun2()
    return x
print(myfunc1())

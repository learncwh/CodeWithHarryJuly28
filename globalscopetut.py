"""l=100 #it is a global variable
def function1(n):
    #l=5 #it is a local variable
    m=3 #it is a local variable
    global l
    l=l+1
    print(n,"Value of l is:",l,"it is a local variable")

    print(n,"Value of m is:",m,"it is a local variable")

function1("Hello")
print("Value of l after using function is:",l)
"""
x=788
def harry():
    x=20 # x is local variable for harry function

    def rohan():
        global x #global x will create a value outside over nested functions
        x+=1 #x is local variable for rohan function
        print("Value of x", x)

    print("Before Calling Rohan value of x is ::",x)
    rohan()
    print("After calling Rohan value of x is ::",x)

harry()
print(x)
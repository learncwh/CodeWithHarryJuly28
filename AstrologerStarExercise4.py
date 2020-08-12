x=int(input("Enter the number to be used:"))
y=int(input("Enter choice:"))
if y==1:
    for i in range(x):
        for j in range(i+1):
            print("*",end="")
        print(" ")
    """for j in range(i):
        print(j)"""
elif y==0:
    for p in range(x):
        for q in range(x,p,-1):
            print("*",end="")
        print("")



x=int(input("Enter the first number:"))
y=int(input("Enter the second number"))
oper=input("Enter the operation to be performed (*,+,/):::")
if oper=="+":
    if (x==56 and y==9) or (x==9 and y==56):
        print("Sum is 77")
    else:
        sum=x+y
        print("Sum is ",sum)
elif oper=="*":
    if (x==45 and y==3) or (y==45 and x==3):
        print("Product is 555")
    else:
        prod=x*y
        print("Product is",prod)
elif oper=="/":
    if x==56 and y==6:
        print("Quotient is 4")
    else:
        quot=x/y
        print("Quotient is",quot)




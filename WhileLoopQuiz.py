while(True):
    x=int(input("Enter any number:"))
    if x==100 or x>100:
        print(x,"Congrats you hve reached the limit")
        break
    elif x<25:
        print("Try Again")
        continue

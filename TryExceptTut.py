x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
def add(x,y):
    try:
        z=x+y
        return z
    #except Exception as e:
      #  print(e)
    except:
        print("Hello")

addition=add(x,y)
print("Answer is ",addition)

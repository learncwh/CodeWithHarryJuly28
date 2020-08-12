list=[int,float,"a","b","56",67,7,1,2]
for item in list:
    if type(item)==int and item>6:
        print(item)
    else:
        print("")
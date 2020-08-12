mystr="harjeet is a good boy"
print(mystr[0:4]) #starts with 0 but will end with 3.Will run through 0,1,2,3
print(mystr[0:100:3]) #it will skip 1 character and print it.Note:When we see 2,we will skip upto n-1 times.In this case it is 2 so we will skip 1 char
print(mystr.__contains__("b"))#check whether the string has argument value
print(mystr.capitalize())#capitalizes the first letter
print(mystr.endswith("boy")) #check the string which ends with
print(mystr.upper()) #converts the whole string to upper case
print(mystr.casefold())#converts the whole string to lower case
print(len(mystr))
print(mystr.count("h"))
print(mystr.replace("is","are"))
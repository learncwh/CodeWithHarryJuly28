s=input("Enter the string")
while("x" in s) or ("o" in s) or ("X" in s) or ("O" in s):
    print("Shit")
    break
print(s.count("x"))
print(s.count("o"))
print(s.count("X"))
print(s.count("O"))

if s.count("x")==s.count("X"):
    print("Hurray")
else:
    print("BC")
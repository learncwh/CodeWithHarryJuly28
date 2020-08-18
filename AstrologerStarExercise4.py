x = int(input("Enter the number to be used:"))
y = int(input(
    "Enter choice:"))  # 1 is for TRUE(will print in ascending order) and 0 is for FALSE(will print in descending order).
if y == 1:
    for i in range(x):
        for j in range(i + 1):
            print("*", end="")
        print("")

elif y == 0:
    for p in range(x):
        for q in range(x, p, -1):
            print("*", end="")
        print("")

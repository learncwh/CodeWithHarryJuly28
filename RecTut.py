"""def print2(str):
    print2("Rohan")
    print("My name is ",str)

print2("Harjeet")"""

"""def factorial(n):
    fact=1
    for i in range(n):
        fact=fact*(i+1)
    return fact

n=int(input("Enter the number:"))
print(factorial(n))
"""


def print_using_recursive(n):
    if n == 1:
        return 1
    else:
        return n + print_using_recursive(n - 1)


n = int(input("Enter the number"))
print(print_using_recursive(n))

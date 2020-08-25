"""Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890" """


def create_phone_number():
    print("(", list1[0], list1[1], list1[2], ")", " ", list1[3], list1[4], list1[5], "-", list1[6], list1[7], list1[8],
          list1[9])


list1 = []
while (True):
    a = int(input("Enter the number:"))
    if a < 10:
        list1.append(a)
        if len(list1) > 11:
            print("Sorry,you cannot enter more")
            break
    print(list1)
    print("Length of list is ", len(list1))
create_phone_number()

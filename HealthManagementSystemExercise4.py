def getdate():
    import datetime
    return str(datetime.datetime.now())

def ExerciseForCust1(exer):
    f=open("ExCustomer1.txt","a+")
    f.write("\n")
    f.write(getdate())
    f.write("\t Client's workout for today:-->")
    f.write(exer)
    f.close()

def ExerciseForCust2(exer):
    f = open("ExCustomer2.txt", "a+")
    f.write("\n")
    f.write(getdate())
    f.write("\t Client's workout for today:-->")
    f.write(exer)
    f.close()

def ExerciseForCust3(exer):
    f = open("ExCustomer3.txt", "a+")
    f.write("\n")
    f.write(getdate())
    f.write("\t Client's workout for today:-->")
    f.write(exer)
    f.close()

def DietForCust1(diet):
    f = open("DietCustomer1.txt", "a+")
    f.write("\n")
    f.write(getdate())
    f.write("\t Client's Diet for today:-->")
    f.write(diet)
    f.close()

def DietForCust2(diet):
    f = open("DietCustomer2.txt", "a+")
    f.write("\n")
    f.write(getdate())
    f.write("\t Client's Diet for today:-->")
    f.write(diet)
    f.close()

def DietForCust3(diet):
    f = open("customer2.txt", "a+")
    f.write("\n")
    f.write(getdate())
    f.write("\t Client's Diet for today:-->")
    f.write(diet)
    f.close()


print("Welcome to the GYM")
cust1 = input("Enter the name of customer1:")
cust2 = input("Enter the name of customer2:")
cust3 = input("Enter the name of customer3:")
while cust1.isalpha() or cust2.isalpha() or cust3.isalpha():
    choiceDorE = input("Do you want to enter Diet or Exercise:") #asking whether to add Diet or Exercise
    if choiceDorE == 'Exercise' or choiceDorE == '1':
        choiceCust = input("For which customer do you want to enter the info:") #asking about the choice of customer
        if choiceCust == cust1:
            exer=input("Which exercise you want to enter::")
            ExerciseForCust1(exer)
        elif choiceCust == cust2:
            exer = input("Which exercise you want to enter::")
            ExerciseForCust2(exer)
        elif choiceCust == cust3:
            exer = input("Which exercise you want to enter::")
            ExerciseForCust3(exer)
        else:
            break
    elif choiceDorE == 'Diet' or choiceDorE == '0' or choiceDorE.capitalize():
        choiceCust = input("For which customer do you want to enter the info:")
        if choiceCust == cust1:
            diet=input("Enter the diet for customer 1::")
            DietForCust1(diet)
        elif choiceCust == cust2:
            diet = input("Enter the diet for customer 1::")
            DietForCust2(diet)
        elif choiceCust == cust3:
            diet = input("Enter the diet for customer 1::")
            DietForCust1(diet)
        else:
            break




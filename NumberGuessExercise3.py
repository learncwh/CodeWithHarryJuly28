#welcome to the guessing game
numguess=5
attempt=5
while(True):
    x=int(input("Enter the number to be guessed:"))
    attempt-=1
    if attempt==0:
        print("Sorry max attempts reached..GAME OVERRRRR")
        break
    elif x==numguess:
        print("Congratulations you have guessed it right")
        print("No. of attempts remaning:",attempt)
        break
    elif x<numguess:
        print("You have guessed a smaller number")
        print("No. of attempts remaning:", attempt)
        continue
    elif x>numguess:
        print("You have guessed a bigger number")
        print("No. of attempts remaning:", attempt)
        continue


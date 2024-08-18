import random
Guess = random.randint(1,6)
print("You have 3 chances.")
i = 1
while( i<=3 ):
    User_Num = int(input("Guess the number between 1 to 6 : "))
    if Guess == User_Num:
        print("Correct")
        break
    else:
        print("Try Again")    
    
    i += 1
    
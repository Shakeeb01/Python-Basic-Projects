First_Num = int(input("Enter the first Number : "))
Second_Num = int(input("Enter the Second Number : "))
Operator = input("Choose the Operator: [ + , - , * , / ] ")


if Operator == '+':
    print(First_Num + Second_Num)
elif Operator == '-':
    print(First_Num - Second_Num)    
elif Operator == '*':
    print(First_Num * Second_Num)    
elif Operator == '/':
    print(First_Num / Second_Num)    
else:
    print("Invalid inputs")    
import time
User_Name = input("Enter Your Name: ") # User Name.
Pin = int(input("Enter Your Pin: "))  # User Account pin.
Account_Balance = 0    # User Account's Balance.


# this is to deposit.
def Deposit_Money():
    global Account_Balance
    user_pin = int(input("Enter Your Pin: "))
    if user_pin == Pin:
        Deposit_Amount = int(input("Enter your amount that you want to deposit: $"))
        Account_Balance += Deposit_Amount
        print(f"Deposit of ${Deposit_Amount} Successfull!")
        print(f"Your total balance is ${Account_Balance}")
    else:
        print("Pin is incorrect.Please Try Again.")


# This is withdraw.
def withdraw_Money():
    global Account_Balance
    user_pin = int(input("Enter Your Pin: "))
    if user_pin == Pin:
        Withdraw_Amount = int(input("Enter your amount that you want to withdraw: $"))
        if Account_Balance == 0:
            print("You account shows ZERO balance.")
        elif Withdraw_Amount >  Account_Balance:
            print("Insufficient Balance.")
        else:
            Account_Balance -= Withdraw_Amount
            print(f"Withdraw of ${Withdraw_Amount} Successfull!")
            print(f"Your remaining balance is ${Account_Balance}")
    else:
        print("Pin is incorrect.Please Try Again.")
 
# this is to check balance.
def check_balance():
    user_pin = int(input("Enter Your Pin: "))
    if user_pin == Pin:
        if Account_Balance == 0:
            print("You account shows ZERO balance.")
        else:
            print(f"Your total balance is ${Account_Balance}")
    else:
        print("Pin is incorrect.Please Try Again.")  
 
 
# this is get loan.
def get_loan():
    global Account_Balance
    user_pin = int(input("Enter Your Pin: "))
    if user_pin == Pin:
        if Account_Balance < 50000:
            Loan_Amount = int(input("Enter the amount of for Loan: $"))
            Account_Balance += Loan_Amount
            print(f" ${Loan_Amount} Loan Added Sucessfully!")
        else:
            print("You have enough balance.You are not eligible for loan.")    
    else:
        print("Pin is incorrect.Please Try Again.")





def main():
    while True:
        print("\n-: Your Pocket Bank :- \n")
        print("1. Deppsit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Get Loan")
        print("5. Exit \n")
            
        User_Choice = input("What do you want to do? ")
        if User_Choice == '1':
            Deposit_Money()
        elif User_Choice == '2':
            withdraw_Money()    
        elif User_Choice == '3':
            check_balance()    
        elif User_Choice == '4':
            get_loan()
        elif User_Choice == '5':
            user_pin = int(input("Enter you pin:"))
            if user_pin == Pin:
                print("Exiting.....") 
                time.sleep(3)
                print("Good bye!")   
                break
            else:
                print("Pin is incorrect.Please Try Again.")
        else:
            print("Invalid Option.Try Again.")
            
            



    
main()


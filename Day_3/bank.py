class BankAccount:
    def __init__(self,AccountName,InitalBalance = 0):
        self.Name = AccountName
        self.Balance = InitalBalance
        print("\nAccount Created :")
        print(f"'{self.Name}' \nAccount Balance ${self.Balance:.2f}")
        
    # this will add the balance
    def deposit(self,depositAmount):
        self.Balance = self.Balance + depositAmount
        print("\nDeposit Successfull!")
        print(f"You have deposit ${depositAmount:.2f}")
        print(f"Your New balance is ${self.Balance:.2f}\n")
    # this is to withdraw balance from your account. 
    def withdraw(self,withdrawAmount):
        if withdrawAmount <= self.Balance:
            self.Balance = self.Balance - withdrawAmount
            print("Withdraw successfull!")
            print(f"Your New balance is ${self.Balance:.2f}\n")
        else:
            print("Widthdraw unsuccessfull!")
            print(f"Sorry you dont have enough balance to withdraw ${withdrawAmount:.2f}")    
            print(f"You Balance is ${self.Balance:.2f}\n")
            

# First Account
Account_1 = BankAccount("Shakeeb ur Rehman")
Account_1.deposit(3000)

# Second Account

Account_2 = BankAccount("Crictiano Ronaldo")
Account_2.deposit(10000)
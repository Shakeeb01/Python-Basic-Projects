Users_List = []
# this will create account
def Create_Account():
    Name = input("Enter your name : ")
    Email = input("Enter your email : ")
    Password = input("Enter your password : ")
    Balance = (input("How much money do you to want to Deposit?"))
    
    User_info = {
        "Name":Name,
        "Email":Email,
        "Password":Password,
        "Balance":Balance
    }
    Users_List.append(User_info)
    
# this will view account
def View_Account():
    if Users_List:
        for i in Users_List:
            print(i)
            print()
    else:
        print("First Create your account")    
    
# Main function. 
def Bank():
    while True:
        print("Options:")
        print()
        print("1. Create Account")
        print("2. View Account")
        print("3. Exit")
        print()
        User_Choice = input("What do you want to Do? ")
  
        if User_Choice == "1":
            Create_Account()
        elif User_Choice == "2":
            View_Account()
        elif User_Choice == "3":
            print("Exiting the Bankpy. Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")
    
    
Bank()
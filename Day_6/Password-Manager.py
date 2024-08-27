
def view():
    print()
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            print(line.rstrip())
    print()

def add():
    name = input("Account Name: ")
    pwd =  input("Password: ")
    
    with open('passwords.txt','a') as f:
        f.write(f'{name} || {pwd}\n')



def main():
    while True:
        Options = input("1. Add a Password\n2. View All\n3. Quit\n")
        if Options == "1":
            add()
            print("Password Added Sucessfully!")
            print()
        elif Options == "2":
            view()
            print()
        elif Options  == "3":
            break 
        else:
            print("Invalid Option! ")
            
                        
while True:              
    main_pwd = input("Enter your 'MASTER' password : ")
    if len(main_pwd) < 6:
        print("Password Lenght should be 6 or greater.")
    else:
        main()
        break                            
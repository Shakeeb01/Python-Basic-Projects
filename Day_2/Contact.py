All_Contacts = []

def Add_Contact():
    print()
    Name = input("Enter Full Name : ")
    Number = input("Enter the Mobile Number : ")
    
    New_Contact = f"'{Name} => {Number}'"
    All_Contacts.append(New_Contact)
    print("Contact Added Successfully!")

def Delete_Contact():
        print()
        for i,contact in enumerate(All_Contacts,start=1):
            print(f"[{i} {contact}]")  
        print()    
        del_index = int(input("Which contact do you want to delete? "))-1
        All_Contacts.pop(del_index)   
        print("Contact is deleted. ")
        
def View_Contacts():
    print()
    if All_Contacts:
        for i,contact in enumerate(All_Contacts,start=1):
            print(f"[{i} {contact}]")     
    else:
        print("Please add contact. ")    
        
        
def Contact():
    while True:
        print()
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        print()
        
        user_choice = input("Choose an option: ")
        if user_choice == "1":
            Add_Contact()
        elif user_choice == "2":
            View_Contacts()    
        elif user_choice == "3":
            Delete_Contact()
        elif user_choice == "4":
            print("Good bye! ")
            break
        else:
            print("Choose a Option by Number: ")
 
Contact()            
           
    
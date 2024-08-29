import os
# this will create file
def create_file(file_name):
    try:
        with open(file_name,'x') as f:
            print(f"created {file_name} successfully!")
    except FileExistsError:
        print(f"{file_name} already exist.")
        
    except Exception as E:
        print("An Error Occured.")
        
# this will view all the files. 
def view_all_files():
    files = os.listdir()
    if not files:
        print("No file found.")
    else:
        print("files in directory.")
        for number , file in enumerate(files,start=1):
            print(f'{number} : {file}')                        
        

# this is to delete file        
def delete_file(file_name):
    try:
        os.remove(file_name)        
        print(f"{file_name} has been deleted successfully")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occured.  ")        
        
        
# this is to read file
def read_file(file_name):
    try:
      with open(file_name,'r') as f:
          content = f.read()
          print(f"content of '{file_name}' : {content}")
    except FileNotFoundError:
        print(f"{file_name} not found.")      
    except Exception as e:
        print("An error occured.")    
 
 
# this is to edit file         
def edit_file(file_name):
    try:
        with open(file_name,"a") as f:
            content = input("Enter data to add : ")
            f.write(content + "\n")
            print(f"content added to {file_name} succesfully!")        
    except FileNotFoundError:
        print(f"{file_name} not found.")      
    except Exception as e:
        print("An error occured.") 
        
        
# main function        
def main():
    while True:
        print()
        print("File Management Application.")
        print()
        print("1. Create File")
        print("2. View All Files")
        print("3. Delete File")
        print("4. Read File")
        print("5. Edit File")
        print("6. Quit")
        print()
        
        choice = int(input("Enter an option (1-6) : "))
        
        if choice == 1:
            file_name = input("Enter the file name :")
            create_file(file_name)   
        elif choice == 2:
            view_all_files()
        elif choice == 3:
            view_all_files()
            file_name = input("Enter the name of file you want to delete : ")
            delete_file(file_name) 
        elif choice == 4:
            view_all_files()
            file_name = input("Which file do you want to read : ")
            read_file(file_name)    
        elif choice == 5:
            view_all_files()
            file_name = input("Enter the file name that you want to edit : ")
            edit_file(file_name)
        elif choice  == 6:
            print("Closing the application...")
            break
        else:
            print("Invalid Option!...")
            
        
        
 
# calling the main funtion. 
if __name__ == "__main__":
    main()                        
                
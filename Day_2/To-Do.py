
ToDo_List = []

# this will add new todo
def Add_Todo():
    Todo = input("Enter Your ToDo Task: ")
    ToDo_List.append(Todo)
    print("Todo added Successfully!")

# this will delete the todo from the given index.
def delete_Todo():
    index = int(input("Enter the index of todo that you want to delete: ")) -1
    if index < len(ToDo_List):
        deleted_ToDo = ToDo_List.pop(index)
        print(f"ToDo '{deleted_ToDo}' deleted successfully!")

   
   
def View_List():
    if ToDo_List:
        print("Here are your tasks:")
        for i, todo in enumerate(ToDo_List, start=1):
            print(f"{i}. {todo}")
    else:
        print("No todo available.")    
        
        
# main function
def Start_ToDo():
    while True:
        print("\nToDo Options:")
        
        print("1. Add ToDo")
        print("2. Delete ToDo")
        print("3. View List")
        
        choice = int(input("Enter your option: "))
        
        if choice == 1:
            Add_Todo()
        elif choice == 2:
            delete_Todo()
        elif choice == 3:
            View_List()    
 
Start_ToDo()        
# Initilising Dictionary

student_grades = {}

# Addd new student
def add_student(name,grade):
    student_grades[name] = grade
    print(f"Added {name} with a {grade}")
    
# update the student 
def update_Student(name,grade):
    if name in student_grades:
        student_grades[name] = name
        print(f"Updated {name} with a {grade}")
    else:
        print(f"{name} is not found .")
# delete the student 
def delete_Student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted.")    
    else:
        print(f"{name} is not found.")    
        
# view all students        

def view_all_Students():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name},{grade}")
        else:
            print("No student found.")     
                   
                   
                   
def main():
    while True:
        print()
        print("1. Add Student")                   
        print("2. Update Student")                   
        print("3. Delete Student")                   
        print("4. View All Students")                   
        print("5. Exit") 
        print()
        
        User_choice = int(input("What do you want to do ? "))
        if User_choice == 1:
            name = input("Enter student name : ")
            grade = int(input("Enter student grade : "))
            add_student(name,grade)
        elif User_choice == 2:
            name = input("Enter student name : ")
            grade = int(input("Enter student grade : "))
            update_Student(name,grade)
        elif User_choice == 3:
            name = input("Enter a student name : ")
            delete_Student(name)
        elif User_choice == 4:
            view_all_Students()
        elif User_choice == 5:
            print("GoodBy!")
            break  
        else:
            print("Invalid option!")              
    
main()    
                      
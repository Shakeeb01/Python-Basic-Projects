notes = []  # list of empty notes later we will add notes.

# this will add note to our list.
def add_note():
    New_Note = input("Enter your note: ")
    notes.append(New_Note)
    print("Note added successfully!")

# This will Delete the note from notes list.
def delete_note():
    view_notes()
    index = int(input("Enter the index of the note to delete: ")) - 1 # 4 - 1 = 3
    if  index < len(notes):
        deleted_note = notes.pop(index)
        print(f"Note '{deleted_note}' deleted successfully!")
    else:
        print("Invalid index! Please try again.")


# this will update the notes
def update_note():
    view_notes()
    index = int(input("Enter the index of the note to update: ")) - 1
    if  index < len(notes):
        updated_note = input("Enter the updated note: ")
        notes[index] = updated_note
        print("Note updated successfully!")
    else:
        print("Invalid index! Please try again.")


# by this we will see our all notes
def view_notes():
    if notes:
        print("Here are your notes:")
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note}")
    else:
        print("No notes available.")


# Main function.
def notebook():
    while True:
        print("\nNotebook Options:")
        print("1. Add Note")
        print("2. Delete Note")
        print("3. Update Note")
        print("4. View Notes")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            delete_note()
        elif choice == "3":
            update_note()
        elif choice == "4":
            view_notes()
        elif choice == "5":
            print("Exiting the notebook. Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")


# Run the notebook function to start the program
notebook()

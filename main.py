from pathlib import Path 

parent_folder = Path(__file__).parent # this gets the folder of the file which runs the program
storage_folder = parent_folder/"storage" # this is the location of the new storage folder which will store the notes
storage_folder.mkdir(exist_ok=True) # This actually creates the new storage folder 

notes_file = storage_folder/"notes.txt" # The location of the notes text file
notes_file.touch(exist_ok=True) # Creates the note.txt file from the above path address

print("Welcome to your Customized Note Editor: ")
while True:
    print()
    print("Please choose from the options below: ")
    print("Enter 1 for adding a note ")
    print("Enter 2 for reading your existing notes")
    print("Enter 3 to restart and add completely new notes")
    print("Enter 4 to exit")
    print()
    
    option = input("Please enter your option: ").strip()
    
    match option:
        case "1":
            user_note = input("Please enter your note:  ")
            with open(notes_file,"a") as note:
                note.write("\n")
                note.write(user_note)
            print("Added your note successfully!")    
            
        case "2":
            print("Your existing notes are: ")
            print()
            with open(notes_file,"r") as reading:
                content =reading.read()
            print(content)    
            
        case "4":
            break
        
        case "3":
            print("Deleting your old notes to give you new fresh start")
            new_text = input("Enter your brand new notes:  ")
            with open(notes_file,"w") as newer:
                newer.write(new_text)
            print("Added the completely brand new notes!")            
        case _:
            print("Please enter a valid option")
                        

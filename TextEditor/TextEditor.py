# Notepad style application that can open, edit, and save text documents. 
# Optional: Add syntax highlighting and other features.

import os

def open_file():
    while True:
        try:
            path = input("Where is your file located?\n")
            os.chdir(path)
            name = input("What is the file called?\n")
            file = open(name, "w+")
            print("File opened successfully.")
            break
        except:
            print("Try again.")
            continue
    return file

def new_file():
    while True:
        try:
            path = input("Where would you like to create your file?\n")
            os.chdir(path)
            name = input("What would you like to name it?\n")
            file = open(name, "w+")
            print("File created successfully.")
            break
        except:
            print("Try again.")
            continue
    return file

def read_file(file):
    print("Opening file in view mode...\n")
    file.seek(0)
    for lines in file:
        print(lines)
        pass
    pass

def edit_file(file):
    print("Opening file in edit mode...\n")
    while True:
        choice = input("Would add your changes to the beginning (1) or end (2) of the file or replace all text (3)?\n")
        if choice == "1":
            file.seek(0)
            break
        elif choice == "2":
            file.seek(2)
            break
        elif choice == "3":
            file.seek(0)
            file.truncate()
            break
        else: 
            print("Invalid input.")
            continue
    print("Type $quit to end edit mode.\n")
    text = ""
    while text != "$quit":
        text = input()
        if text == "$quit":
            print("File saved. Exiting edit mode...")
            break
        else:
            file.write(text + "\n")
            continue
    pass

def delete_file(file):
    choice = input("This action is permanent, are you sure you want to delete {}? Enter y/n\n".format(file.name))
    if choice == "y":
        os.remove(file.name)
        print("File deleted.")
        main()
        pass
    else:
        print("File was not deleted.")
        pass
    pass

def rename_file(file):
    name = input("What would you like it to be named?\n")
    os.rename(file.name, name)
    print("File renamed to " + name)
    pass

def main():
    print("MyTextEditor")
    # Get a file:
    while True:
        choice = input("What would you like to do?\n(1) Open a file\n(2) Create a file\n(3) Quit\n")
        if choice == "1":
            file = open_file()
            break
        elif choice == "2":
            file = new_file()
            break
        elif choice == "3":
            print("Goodbye!")
            file.close()
            quit()
            break
        else:
            print("Invalid input.")
            continue
        pass
    # Choose what to do with file:
    while choice != "5":
        choice = input("(1) Read file\n(2) Edit file\n(3) Rename file\n(4) Delete file\n(5) Quit\n")
        if choice == "1":
            read_file(file)
            pass
        elif choice == "2":
            edit_file(file)
            pass
        elif choice == "3":
            rename_file(file)
            pass
        elif choice == "4":
            delete_file(file)
            pass
        elif choice == "5":
            print("Goodbye!")
            file.close()
            quit()
            break
        else:
            print("Invalid input.")
            continue
        pass
    file.close()
    pass

main()

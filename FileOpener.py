import os

current_directory = None

def list_subfolders(directory):
    subfolders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    for index, subfolder in enumerate(subfolders):
        print(f"[{index}] {subfolder}")

def open_subfolder(directory, index):
    subfolders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    if index < 0 or index >= len(subfolders):
        print("Invalid index number.")
        return None
    subfolder_path = os.path.join(directory, subfolders[index])
    print(f"Opening subfolder: {subfolder_path}")
    return subfolder_path

def list_files(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for index, file in enumerate(files):
        print(f"[{index}] {file}")

def view_files(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if not files:
        print("No files found in the current directory.")
        return
    for index, file in enumerate(files):
        print(f"[{index}] {file}")

def open_file(directory, index):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if index < 0 or index >= len(files):
        print("Invalid index number.")
        return
    file_path = os.path.join(directory, files[index])
    print(f"Opening file: {file_path}")
    os.startfile(file_path)  # Opens the file with the default file viewer on Windows

# Directory path
directory = '/path/to/directory'

while True:
    print("\n1. List subfolders")
    print("2. Open subfolder")
    print("3. View files")
    print("4. Open file")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        list_subfolders(directory)
    elif choice == '2':
        index = int(input("Enter the index number of the subfolder: "))
        current_directory = open_subfolder(directory, index)
    elif choice == '3':
        if not current_directory:
            print("No subfolder is open. Please open a subfolder first.")
            continue
        view_files(current_directory)
    elif choice == '4':
        if not current_directory:
            print("No subfolder is open. Please open a subfolder first.")
            continue
        index = int(input("Enter the index number of the file to open: "))
        open_file(current_directory, index)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

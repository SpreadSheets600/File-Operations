import shutil

def move_files(source_folder, destination_folder):
    # Move each file from the source folder to the destination folder
    for file_name in os.listdir(source_folder):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)

# Prompt the user to input the source and destination directories
source_folder = input("Enter the path to the source folder: ")
destination_folder = input("Enter the path to the destination folder: ")

# Call the function to move files from the source folder to the destination folder
move_files(source_folder, destination_folder)

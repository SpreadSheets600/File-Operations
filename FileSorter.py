import os
import shutil

# Sort Files

def organize_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_extension = os.path.splitext(file)[1]
            target_directory = os.path.join(directory, file_extension[1:].upper() + " Files")

            if not os.path.exists(target_directory):
                os.mkdir(target_directory)

            source_path = os.path.join(root, file)
            target_path = os.path.join(target_directory, file)

            shutil.move(source_path, target_path)
            print(f"Moved {file} to {target_directory}")

    print("File organization completed!")

def main():
    directory = input("Enter the directory path to organize: ")
    organize_files(directory)

if __name__ == "__main__":
    main()

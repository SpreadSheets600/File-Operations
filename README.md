# Python File Operations
**The Programs Available In The Repository Are :**

 - [X] 1. File Sorter
 - [X] 2. File Mover
 - [X] 3. File Opener

---
The Required Modules For The Files To Be Executed Are :

1. `OS Module` - It is a built in module
2. `SHUTIL Module` - It is a built in module
---

The Description Of Each Of The File Is As Follows:

<details>
<summary> 1. File Sorter </summary>

 
This script recursively organizes files in a directory by creating separate folders for each file extension and moving the corresponding files into their respective folders. 

*The Breakdown Of The File :*
> 1.  The script prompts the user to enter a directory path that they want to organize.
> 
> 2.  It uses the `os.walk` function to traverse the specified directory and its subdirectories, retrieving information about all the files and directories within it. 
>    
> 3.  For each file encountered, the script extracts the file extension using `os.path.splitext(file)[1]`.    
> 
> 4.  It creates a target directory for the specific file extension, using the uppercase extension as the directory name. If the target directory doesn't already exist, it creates it using `os.mkdir(target_directory)`.  
>   
> 5.  The script moves each file to its corresponding target directory using `shutil.move`, and it prints a message indicating the file has been moved. Once all the files have been processed, it prints "File organization completed!" to signify the completion of the organization process.
</details>

<details>
<summary> 2. File Mover </summary>

 
This script defines a function move_files that moves all files from a source folder to a destination folder, and then prompts the user to input the paths for the source and destination folders to execute the function.

*The Breakdown Of The File :*
> 1. The code begins by importing the shutil module, which provides functions for file operations, including moving files.
>   
> 2. The code defines a function named `move_files` that takes two parameters: `source_folder` and `destination_folder`. This function is responsible for moving files from the source folder to the destination folder.
>   
> 3. Within the `move_files` function, a `for` loop is used to iterate over each file in the source folder. It uses `os.listdir(source_folder)` to retrieve a list of file names in the source folder.
>   
> 4. For each file in the source folder, the code constructs the source path by joining the `source_folder` and the `file_name` using `os.path.join()`. Similarly, the destination path is constructed by joining the `destination_folder` and the `file_name`.
>   
> 5. Inside the loop, the `shutil.move()` function is called to move the file from the source path to the destination path. This function moves the file to the destination folder and removes it from the source folder.
>   
> After defining the function, the code prompts the user to enter the paths for the source and destination folders using the `input()` function. Finally, the `move_files` function is called with the provided source and destination folders to move the files.

</details>

<details>
<summary> 3. File Viewer </summary>

 
The script provides a user-friendly interface for navigating and exploring subfolders, viewing files within a selected subfolder, and opening specific files using the default file viewer on the system.

*The Breakdown Of The File :*
> 1. List Subfolders: The program starts by listing all the subfolders present in the specified directory. It displays each subfolder along with an index number, allowing the user to identify and select a subfolder of interest.
>   
> 2. Open Subfolder: Once the user selects a subfolder by entering its index number, the program opens that subfolder. It verifies the index entered by the user and constructs the path to the selected subfolder. Then it sets the current_directory variable to the path of the opened subfolder.
>   
> 3. View Files: After opening a subfolder, the user can choose the "View files" option. The program lists all the files present in the currently open subfolder. If there are no files, it informs the user accordingly. Otherwise, it displays each file along with an index number.
>    
> 4. Open File: If the user wants to open a specific file, they can choose the "Open file" option. The program verifies that a subfolder is currently open and prompts the user to enter the index number of the file they wish to open. Once a valid index is entered, the program constructs the path to the selected file within the open subfolder and opens it using the default file viewer on the system.
>   
>  5. Quit: The user has the option to quit the program by selecting the "Quit" option. This exits the program and ends the execution.
 
</details>

GUI Comming Soon :D

# task 1

# Create a Python script that lists all files and subdirectories in a given directory. 
# Your script should prompt the user for the directory path and then display the contents.

# Code Example:
# import os

# def list_directory_contents(path):
#     # List and print all files and subdirectories in the given path
# Expected Outcome:
# The script should correctly list all files and subdirectories in the specified directory.
# Handle exceptions for invalid paths or inaccessible directories.

import os

def list_directory_contents(path):
    try:
        content = os.listdir(path)
        
    except FileNotFoundError:
        
        print("Directory not found")
        
    except PermissionError:
        
        print("No permission")
        
    
    return content

path = input("Enter a directory path: ")
print(list_directory_contents(path))


# task 2
# Write a Python program that reports the sizes of all files in a specific directory. 
# The program should ask the user for a directory path and then print each file's 
# name and size within that directory.

# Code Example:
# def report_file_sizes(directory):
#     # Iterate through files in the directory and print their names and sizes
# Expected Outcome:
# Your program should display the name and size (in bytes) of each file in 
# the given directory. Ensure that the program only reports on files, not 
# directories, and handles any errors gracefully.


def report_file_sizes(directory):
    
    try:
        for file in os.listdir(directory):
            filename = os.path.join(directory, file)
            
            if os.path.isfile(filename):
                
                size = os.path.getsize(filename)
                
                print("File Name: ", filename, " size: ", size)
                
                
    except FileNotFoundError:
        
        print("Directory not found")
        
    except PermissionError:
        
        print("No permission")
        
directory = input("Enter a directory path: ")
report_file_sizes(directory)


# task 3
# Develop a Python script that counts the number of files of each 
# extension type in a directory. For instance, in a directory with five '.txt' 
# files and three '.py' files, the script should report "TXT: 5" and "PY: 3".

# Code Example:
# def count_file_extensions(directory):
#     # Count and print the number of files of each extension type in the directory
# Expected Outcome:
# The script should accurately count and display the number of files 
# for each extension type in the specified directory. Handle different 
# cases of file extensions (e.g., '.TXT' and '.txt' should be considered the same).

def count_file_extensions(directory):
    
    try:
        extension_list = {}
        
        for file in directory:
            
            extension = os.path.splitext(file)
            
            extension = extension.lower()
            
            if extension[1] in extension_list:
                
                extension_list[extension[1]] = extension_list[extension[1]] + 1
            
            else:
                extension_list[extension[1]] = 0
                
    except FileNotFoundError:
        
        print("Directory not found")
        
    except PermissionError:
        
        print("No permission")
        
    return extension_list
        
directory = input("Enter a directory path: ")
print(count_file_extensions(directory))
                
    
                
            
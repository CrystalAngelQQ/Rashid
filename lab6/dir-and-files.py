# Python Directories and Files exercises
import os
import shutil


# Write a Python program to list only directories, files and all directories, files in a specified path.
def list_files(specified_path: str) -> None:
    if not os.path.exists(specified_path):
        print("Path does not exist.")
        return

    for root, dirs, files in os.walk(specified_path):
        print(f"Path: {root}")
        if dirs:
            print("Directories: ")
            for dir_name in dirs:
                print(dir_name)
        if files:
            print("Files: ")
            for file_name in files:
                print(file_name)


path = input("Enter the path to list: ")
list_files(path)


# Write a Python program to check for access to a specified path. Test the existence, readability, writability and
# executability of the specified path
def check_access(specified_path: str) -> None:
    if not os.path.exists(specified_path):
        print("Path does not exist.")
        return

    print(f"Checking access for {specified_path}")

    exists: bool = os.path.exists(specified_path)
    readable: bool = os.access(specified_path, os.R_OK)
    writable: bool = os.access(specified_path, os.W_OK)
    executable: bool = os.access(specified_path, os.X_OK)

    print(f"Exists: {exists}")
    print(f"Readable: {readable}")
    print(f"Writable: {writable}")
    print(f"Executable: {executable}")


path = input("Enter the path to check access for: ")
check_access(path)


# Write a Python program to test whether a given path exists or not. If the path exist find the filename and
# directory portion of the given path.
def path_info(specified_path: str) -> None:
    if not os.path.exists(specified_path):
        print("Path does not exist.")
        return

    print(f"Checking path info for {specified_path}")
    dir_name, file_name = os.path.split(specified_path)
    print(f"Directory: {dir_name}")
    print(f"Filename: {file_name}")


path = input("Enter the path to get info for: ")
path_info(path)


# Write a Python program to count the number of lines in a text file.
def count_lines(specified_path: str) -> int:
    if not os.path.exists(specified_path):
        print("Path does not exist.")
        return

    if not os.path.isfile(specified_path):
        print(f"{specified_path} is not a file.")
        return

    result: int = 0
    with open(specified_path, "r") as file:
        for _ in file:
            result += 1
    return result


file_path = input("Enter the path to the file to count lines: ")
num_lines = count_lines(file_path)
print(f"Number of lines in {file_path}: {num_lines}")


# Write a Python program to write a list to a file.
def write_list_to_file(specified_path: str, list_data: list) -> None:
    with open(specified_path, "w") as file:
        for item in list_data:
            file.write("\n".join(list_data))


file_path = input("Enter the path for the new file: ")
data = input("Enter the list of items separated by spaces: ").split()
write_list_to_file(file_path, data)
print(f"List written to {file_path}.")


# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
def generate_files() -> None:
    for i in range(ord("A"), ord("Z") + 1):
        letter: str = chr(i)
        filename = f"{letter}.txt"
        with open(filename, "w") as file:
            file.write(letter)


generate_files()


# Write a Python program to copy the contents of a file to another file
def copy_file(source_path: str, dest_path: str) -> None:
    if not os.path.exists(source_path):
        print("It does not exist.")
        return

    if not os.path.isfile(source):
        print("It is not a file.")
        return

    with open(source_path) as file:
        with open(dest_path, "w") as new_file:
            new_file.write(file.read())


source = input("Enter the source filename to copy: ")
dest = input("Enter the destination filename to copy to: ")
copy_file(source, dest)


# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path
# exists or not.
def delete_file(path: str):
    if not os.path.exists(specified_path):
        print("It does not exist.")
        return
    if not os.access(path, os.W_OK):
        print(f"You do not have permission to delete {path}.")
        return
    os.remove(path)
    print(f"{path} has been deleted successfully.")

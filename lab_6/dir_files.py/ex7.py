import os

def copier():
    string = r"C:\Users\nuril\PP2_labs\lab_6\dir_files.py\text.txt"

    if not os.path.exists(string):
        print(f"Error: The file '{string}' does not exist.")
        return


    with open(string, "r", encoding="utf-8") as file:
        data = file.read()

    copy_path = string.replace(".txt", "_1.txt")

    with open(copy_path, "w", encoding="utf-8") as file_copy:
        file_copy.write(data)

    print(f"File copied successfully! New file: {copy_path}")

copier()


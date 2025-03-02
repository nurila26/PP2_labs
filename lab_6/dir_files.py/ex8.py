import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):  
            try:
                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.") 
            except Exception as e:
                print(f"Error deleting file: {e}")
        else:
            print("You do not have write access to this file.")
    else:
        print(f"File '{file_path}' does not exist.")


path_delete = r"C:\Users\nuril\PP2_labs\lab_6\dir_files.py\text_1.txt"

delete_file(path_delete)


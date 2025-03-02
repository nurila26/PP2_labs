import os
import string

with open(r"C:\Users\nuril\PP2_labs\lab_6\dir_files.py\text.txt", encoding="utf-8") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
f.close()
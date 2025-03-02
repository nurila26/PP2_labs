def write(list_of_elements):
    with open(r"C:\Users\nuril\PP2_labs\lab_6\dir_files.py\text.txt", "a+", encoding="utf-8") as f:
        text = "\n"
        for i in list_of_elements:
            text+=str(i)+' '
        f.write(text)
        f.close()
    
 

write([888888, 666666, 26262626, "two", "six", 26])

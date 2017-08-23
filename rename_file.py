import os

def rename():
    file_list = os.listdir(r"C:\Users\BHADMUS\Favorites\Downloads")
    print(file_list)

    for file_name in file_list:
        os.rename(file_name,file_name.translate("0123456789"))

rename()
    

import shutil
import os
from env import source_dir, final_dir

#source Directory
src_dir = source_dir
#Folder directory
parent_dir = final_dir 

dir_name = input("user enter your folder name :")
path = os.path.join(parent_dir, dir_name)
os.mkdir(path)
print("Folder is created!!")
print(path)#destination folder location
shutil.copytree(src_dir, path, dirs_exist_ok=True)
print("all files copied to "+dir_name)
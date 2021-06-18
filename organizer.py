import os
import shutil
source = input("Enter source folder")
files = os.listdir(source)
for i in files:
    name,ext = os.path.splitext(i)
    ext = ext[1:]
    if ext == "":
        continue
    if os.path.exists(source+"/"+ext):
        shutil.move(source+"/"+i,source+"/"+ext+"/"+i)
    else:
        os.makedirs(source+"/"+ext)
        shutil.move(source+"/"+i,source+"/"+ext+"/"+i)
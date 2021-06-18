import os
import shutil
source = input("Enter source folder")
destination = input("Enter the destination folder")
source = source+"/"
destination = destination+"/"
filelist = os.listdir(source)
for i in filelist:
    shutil.copy((source+i),destination)
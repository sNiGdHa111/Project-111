import os
import shutil
from_dir="C:/Users/snigd/Downloads"
to_dir="C:/Users/snigd/Desktop/coding class/wsj/c112"
listOfFiles = os.listdir(from_dir)
print(listOfFiles)
for file_name in listOfFiles:
    name,ext=os.path.splitext(file_name)
    print(name)
    print(ext)
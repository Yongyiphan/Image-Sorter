#Rename this file
from inspect import trace
import shutil
from glob import glob
import os 
from os import listdir
import traceback
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import CustomLogger as CLog




#Image Archive Directory
ArchiveDir = "C:\\Users\\edgar\\Documents\\Image Archive"
CategoriesDir  = ArchiveDir + "\Categories"
PhotoDumpDir = ArchiveDir + "\Photo Dump"

Duplicates = []

MLog = CLog.Set_Custom_Logger("Main", ".\MLogs.log")

def main():
    os.chdir(CategoriesDir)
    FileContents = {key:value for key, value in enumerate(listdir(CategoriesDir)) if os.path.isdir(CategoriesDir + "\\" + value)}
    TotalKeys = len(FileContents.keys())
    os.chdir(PhotoDumpDir)
    PhotoDump = [f for f in listdir(PhotoDumpDir) if os.path.isfile(PhotoDumpDir + "\\" + f ) and  f not in [fn for fn in glob(PhotoDumpDir + "*.txt")]]
    #Filter GIF
    
    TempDumpDir = os.path.join(CategoriesDir, "Temp")
    for photo in PhotoDump:
        try:
            pPath = PhotoDumpDir + "\\" + photo
            des = os.path.join(TempDumpDir, photo)
            displayPhoto(pPath, photo)
            
            print("\n New Sort")
            for k, v in FileContents.items():
                print(f"{k}: {v}")
          
            Input = input("New Location: ")
            
            if Input.lower() == "n":
                TotalKeys += 1
                NewFolder = input("New Folder Name: ") 
                FileContents[TotalKeys] = NewFolder
                NFolderPath = os.path.join(CategoriesDir, NewFolder)
                if not os.path.exists(NFolderPath):
                    os.mkdir(NFolderPath)
                des = os.path.join(NFolderPath, photo)
                if not checkFileExist(pPath, des, NewFolder, TempDumpDir, photo):
                    continue
            else:
                try:
#                    Confirm = input(f"Adding to {FileContents[int(Input)]}? Y /N")
                    des = os.path.join(CategoriesDir ,FileContents[int(Input)], photo)
                    if not checkFileExist(pPath, des, FileContents[int(Input)], TempDumpDir, photo):
                        continue
                except:
                    MLog.critical(traceback.format_exc())
            
            shutil.move(pPath, des)
        except:
            MLog.critical(traceback.format_exc())
            shutil.move(pPath, des)
            continue
    return

def displayPhoto(src, photo):
    plt.title(photo)
    image = mpimg.imread(src)
    plt.imshow(image)
    plt.show(block = False)

# source path | des path | des folder | dump path | photo name
def checkFileExist(src, des, Folder, dump, photo):
    if os.path.exists(des):
        MLog.info(f"Fail to move {photo} to {Folder}")
        des = os.path.join(dump, photo)
        shutil.move(src, des)
        return False
    return True
if __name__ == '__main__':
    
    main()
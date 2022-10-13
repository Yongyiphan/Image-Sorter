from fileinput import filename
import shutil
import PIL
from PIL import Image
import os


Search_Keyword = ["FGO", "Fate"]
Target_Search = []

ImageArchiveDir = "C:\\Users\\edgar\\Documents\\Image Archive"
PhotoDumpDir = os.path.join(ImageArchiveDir, "Photo Dump")
CategoriesDir = os.path.join(ImageArchiveDir, "Categories")


SortedPics = {}
PhotoDumpPics = {}

def resolveDuplicates():
    for dirpath, dir, files in os.walk(CategoriesDir):
        if "Duplicate_Pics" in dirpath:
            continue
        for filenames in files:
            fname = os.path.join(dirpath, filenames)
            if filename in SortedPics.keys():
                print("Existed")
            SortedPics[filenames] = fname
    print(f"\nSorted Pics: {len(list(SortedPics.keys()))}\n")
    for files in os.listdir(PhotoDumpDir):
        PhotoDumpPics[files] = os.path.join(PhotoDumpDir, files)

    common = [c for c in list(SortedPics.keys()) if c in PhotoDumpPics.keys()]
    for c in common:
        shutil.move(PhotoDumpPics[c], os.path.join(CategoriesDir, "Duplicate_Pics"))
    
    print(f"\nDuplicate Pics: {len(common)}\n")
    ...



if __name__ == "__main__":
    resolveDuplicates()
    ...

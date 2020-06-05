import os
from PIL import Image

def listfile(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for d in dirs:
            print(os.path.join(root,d))
        for f in files:
            im = Image.open(f)
            name = f.split(".")[0]
            im.save(name+".jpg", "JPEG")

if __name__ == "__main__":
    listfile()
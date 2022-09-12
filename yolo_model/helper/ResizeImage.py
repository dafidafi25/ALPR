from PIL import Image
import os, sys

path = "D:/Dafi/Training/Yolo/target_image/jpg/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        print(path+item)
        if os.path.isfile(path+item):
            print(item)
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((896,896), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)


if __name__ == '__main__':
    resize()
from PIL import Image
import os, sys

path = "D:/Dafi/Training/Yolo/dataset/plate_number_indonesia/PLATE_RECOGNITION.v5-plate-recognition-v5.yolov5pytorch/test/labels/"
dirs = os.listdir( path )

def rewrite():
    for item in dirs:
        # full_path = os.path.abspath(item)
        new_value = ''
        with open(f'{path}{item}','r') as f:
            for line in f:
                if len(line) > 1 :
                    Curr_Data = line.strip()
                    print(f'Before : {Curr_Data}')
                    new_value += f'{0}{Curr_Data[1:len(line)]}\n'
        
        print(f'------ After =========')
        
        with open(f'{path}{item}','w') as f:
            size = len(new_value)
            if size > 0:
                print(f'{new_value[0:size-1]}')
                f.writelines(new_value[0:size-1])
        
        print(f'========= Next =========')
                


if __name__ == '__main__':
    rewrite()
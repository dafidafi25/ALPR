import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

imgs = os.listdir('D:/Dafi/Training/Yolo/dataset/cars/images')
imgs_train, imgs_val = train_test_split(imgs, test_size=0.05)

df = pd.read_csv('D:/Dafi/Training/Yolo/dataset/cars/annotation.csv')


# ######
import yaml
cwd = 'D:/Dafi/Training/Yolo/dataset/cars/'
data = dict(
    train =  cwd + 'train.txt',
    val   =  cwd + 'val.txt',
    nc    = 1,
    names = ['licence'],
)

with open(cwd + 'bgr.yaml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)
with open(cwd + 'train.txt', 'w') as f:
    for path in imgs_train:
        f.write(cwd+'images/'+path+'/n')
with open(cwd + 'val.txt', 'w') as f:
    for path in imgs_val:
        f.write(cwd+'images/'+path+'/n')


######
for file in imgs:
    file = file.split('.')[0]
    bboxs = []
    for _,row in df[df['file'] == file].iterrows():
        bbox = [str(0), str(row['Xcent']), str(row['Ycent']), str(row['boxW']), str(row['boxH'])]
        bbox = ' '.join(bbox)
        bboxs.append(bbox)
    with open(cwd+'labels/'+file+'.txt', 'w') as f:
        bboxs = '/n'.join(bboxs)
        f.write(bboxs)



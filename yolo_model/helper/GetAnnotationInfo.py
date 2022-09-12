import pandas as pd
import numpy as np
import os
import glob
import xml.etree.ElementTree as ET 

path_an = "D:/Dafi/Training/Yolo/dataset/cars/annotations"

dataset = {
            "xmin":[],
            "ymin":[],   
            "xmax":[],
            "ymax":[],
            "name":[],    
            "file":[],
            "width":[],
            "height":[],
           }

for anno in glob.glob(path_an+"/*.xml"):
    tree = ET.parse(anno)
    
    for elem in tree.iter():
        if 'size' in elem.tag:
            for attr in list(elem):
                if 'width' in attr.tag: 
                    width = int(round(float(attr.text)))
                if 'height' in attr.tag:
                    height = int(round(float(attr.text)))    

        if 'object' in elem.tag:
            for attr in list(elem):
                
                if 'name' in attr.tag:
                    name = attr.text                 
                    dataset['name']+=[name]
                    dataset['width']+=[width]
                    dataset['height']+=[height] 
                    dataset['file']+=[anno.split('/')[-1][0:-4]] 
                            
                if 'bndbox' in attr.tag:
                    for dim in list(attr):
                        if 'xmin' in dim.tag:
                            xmin = int(round(float(dim.text)))
                            dataset['xmin']+=[xmin]
                        if 'ymin' in dim.tag:
                            ymin = int(round(float(dim.text)))
                            dataset['ymin']+=[ymin]                                
                        if 'xmax' in dim.tag:
                            xmax = int(round(float(dim.text)))
                            dataset['xmax']+=[xmax]                                
                        if 'ymax' in dim.tag:
                            ymax = int(round(float(dim.text)))
                            dataset['ymax']+=[ymax]   
data0=pd.DataFrame(dataset)

print(data0['name'].unique())

data0['class']=data0['name'].map({'licence':0})
data0['Xcent']=(data0['xmin']+data0['xmax'])/(2*data0['width'])
data0['Ycent']=(data0['ymin']+data0['ymax'])/(2*data0['height'])
data0['boxW']=(data0['xmax']-data0['xmin'])/data0['width']
data0['boxH']=(data0['ymax']-data0['ymin'])/data0['height']
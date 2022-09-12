import cv2
import torch
import imutils as im
import numpy
import string

# Model Plate Number Localization roboflow_lpr_02
# Model OCR test_linux_training

def main_01():
    # # Model
    print(f'Prepare Model')
    model = torch.hub.load('/home/rio/work/tugas_akhir/ALPR/yolo_model','custom', '/home/rio/work/tugas_akhir/ALPR/yolo_model/runs/train/test_linux_training/weights/best.pt', source='local') 
    print(f'Model Ready')

    # Load Image
    img1 = cv2.imread('/home/rio/work/tugas_akhir/ALPR/images/rio/1.jpg')
    img2 = cv2.imread('/home/rio/work/tugas_akhir/ALPR/images/rio/2.jpg')
    img3 = cv2.imread('/home/rio/work/tugas_akhir/ALPR/images/rio/3.jpg')

    imgs = [img1, img2, img3]


    results = model(img2, size=640)  # inference
    predicts = results.xyxy[0].numpy()
    predicts = predicts.astype(numpy.int64)

def main_02():
    model = torch.hub.load('/home/rio/work/tugas_akhir/ALPR/yolo_model','custom', '/home/rio/work/tugas_akhir/ALPR/yolo_model/runs/train/roboflow_lpr_02/weights/best.pt', source='local') 

# def get_alphabet(self,idx):
#     alphabet_list = list(string.ascii_lowercase)
#     return alphabet_list[idx]

class PlateOCR:
    def __init__(self):
        self.model = torch.hub.load('/home/rio/work/tugas_akhir/ALPR/yolo_model','custom', '/home/rio/work/tugas_akhir/ALPR/yolo_model/runs/train/test_linux_training/weights/best.pt', source='local')

    def get_character(self, img):
        results = self.model(img, size=640)
        predicts = results.xyxy[0].numpy()
        predicts = predicts.astype(numpy.int64)
        if len(predicts) == 0 :
            raise Exception("No Predicted Data")
        for predict in predicts:
            yield predict

    def get_alphabet(self,idx):
        alphabet_list = list(string.ascii_lowercase)
        return alphabet_list[idx].upper()

class PlateLocalization:
    def __init__(self):
        self.model = torch.hub.load('/home/rio/work/tugas_akhir/ALPR/yolo_model','custom', '/home/rio/work/tugas_akhir/ALPR/yolo_model/runs/train/roboflow_lpr_02/weights/best.pt', source='local') 
    
    def get_plate(self,img):
        results = self.model(img, size=640)  # inference
        predicts = results.xyxy[0].numpy()
        predicts = predicts.astype(numpy.int64)
        if len(predicts) == 0 :
            raise Exception("No Predicted Data")
        for predict in predicts:
            xMin = predict[0]
            yMin = predict[1]
            xMax = predict[2]
            yMax = predict[3]
            # # Cropping images
            cropped_img = img[yMin:yMax, xMin:xMax]
            yield cropped_img

if __name__=="__main__":
    # main_01()
    PlateNumberModel = PlateLocalization()
    OCRModel = PlateOCR()
    img = cv2.imread("/home/rio/work/tugas_akhir/ALPR/images/test_new/2 A.jpg")
    plates_array = []
    try:
        plates = PlateNumberModel.get_plate(img)
        for plate in plates:
            plates_array.append(plate)
        
    except Exception as err :
        print(err)

    try:
        for plate in plates_array:
           
            chars = OCRModel.get_character(plate)
            
            char_array = []
            for char in chars:
                char_array.append(char)
            
            char_array.sort(key= lambda x: x[0])
            
            for char in char_array:
                text = char[5]
                if text > 24 : print(OCRModel.get_alphabet(text-11))
                elif text > 9 : print(OCRModel.get_alphabet(text-10))
                elif text == 24 : continue
                else : print(text)
                
    except Exception as err:
        print(err)    
    



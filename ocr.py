import cv2
import pytesseract

image_path4 = 'D:/Dafi/Kerja/Joki TA/Rio/images/dafi/processed_2.jpg'

img = cv2.imread(image_path4)

custom_config = r'--oem 3 --psm 6'
test = pytesseract.image_to_string(img, config=custom_config)
print(test)
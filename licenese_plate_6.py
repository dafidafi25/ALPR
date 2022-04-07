from turtle import distance, width

from cv2 import rectangle
import preprocess as pp
import cv2
import imutils as im
import numpy as np
from skimage.segmentation import clear_border

import pytesseract

def detect_plate(input):
    img = cv2.imread(input)

    img = im.resize(img, width=1080)

    imgGrayscale, img_thresh = pp.preprocess(img)

    cnts = cv2.findContours(img_thresh, cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE)  # find all contours
    cnts = im.grab_contours(cnts)

    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    detectedAr = DetectByAR(imgGrayscale,contours=cnts)

    cv2.imshow("img_thresh",img_thresh)
    
    DetectByVector(imgGrayscale,img_thresh,img)


def DetectByAR(imgGrayscale,contours):
    cv2.drawContours(imgGrayscale,contours,-1,(255,0,0),2)
    cv2.imshow("contoured image", imgGrayscale)
    # for c in contours:
    #     roi = None
    #     (x, y, w, h) = cv2.boundingRect(c)
    #     ar = w / float(h)
    #     clearBorder = False
    #     # check to see if the aspect ratio is rectangular
    #     if ar >= 4 and ar <= 5:
    #         # store the license plate contour and extract the
    #         # license plate from the grayscale image and then
    #         # threshold it
    #         lpCnt = c
    #         licensePlate = imgGrayscale[y:y + h, x:x + w]
    #         roi = cv2.threshold(licensePlate, 0, 255,
    #             cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    #         # check to see if we should clear any foreground
    #         # pixels touching the border of the image
    #         # (which typically, not but always, indicates noise)
    #         if clearBorder:
    #             roi = clear_border(roi)
    #         # display any debugging information and then break
    #         # from the loop early since we have found the license
    #         # plate region
    #         cv2.imshow("ROI",roi)
    #         return(roi)
    return([[None]])

def DetectByVector(gray,thresh,img):
    edged = cv2.Canny(thresh, 150 , 200)
   
    cnts = cv2.findContours(edged, cv2.RETR_EXTERNAL,
                                              cv2.CHAIN_APPROX_NONE)  # find all contours
    cnts = im.grab_contours(cnts)
    filtered_cnts = []
    
    for cnt in cnts:
        x,y,w,h = cv2.boundingRect(cnt)
        width = x+w
        height = y+h

        if(width < 800 and width >200 and w > 20 and w<40 and h<100 and h> 20):
            filtered_cnts.append([x,y,w,h])
            print([x,y,w,h])
                

    distance_threshold = 15 
    uniqueY = []
    for i in range(len(filtered_cnts)):
        if i == 0:
            y = filtered_cnts[i][1]
            uniqueY.append ([y,0])
            continue
        uniquePass = True
        for j in range(len(uniqueY)):
            selisih = abs(uniqueY[j][0] - filtered_cnts[i][1])
            if selisih < distance_threshold:
                uniquePass = False
                uniqueY[j][1]  = uniqueY[j][1]+ 1
        if uniquePass == True:
            uniqueY.append([filtered_cnts[i][1],0])
    most_unique = [0,0]
    for i in range(len(uniqueY)):
        if(uniqueY[i][1] > most_unique[1]):
            most_unique[0] = uniqueY[i][0]
            most_unique[1] = uniqueY[i][1]


    rectangle = []
    x_master = 9999
    y_master = 9999
    w_master = 0
    h_master = 0
    for i in range(len(filtered_cnts)):
        if abs(filtered_cnts[i][1] - most_unique[0]) < distance_threshold:
            rectangle.append(filtered_cnts)
            x = filtered_cnts[i][0]
            y = filtered_cnts[i][1]
            w = filtered_cnts[i][2]
            h = filtered_cnts[i][3]
            # print([x,y,w,h])
            x_master = x if x < x_master else x_master
            y_master = y if y < y_master else y_master
            w_master = w+x if w+x > w_master else w_master
            h_master = y+h if y+h > h_master else h_master
    area = 5

    x_master -= area
    y_master -= area
    w_master += area
    h_master += area

    # cv2.rectangle(img,(x_master ,y_master  ),(w_master ,h_master  ),(255,255,0),2)
    cv2.imshow("Filtered",img)
    cropped = img[y_master:h_master, x_master:w_master]
    cv2.imshow("Cropped",cropped)
    imgGrayscale, img_thresh = pp.preprocess(cropped)
    cv2.imshow("Ready to read",img_thresh)
    print("tesseract : " + pytesseract.image_to_string(img_thresh,config='--psm 11'))




def main():
    # image_path4 = '/Users/dafigumawangpriadi/work/joki_ta/ALPR/images/dafi/22.jpeg' # MAC-Path
    # image_path4 = './images/dafi/35.jpeg' # PC-Path
    # detect_plate(image_path4)
    # cv2.waitKey()
    # image_path1 = 'D:/Dafi/Kerja/Joki TA/Rio/images/mobil/Cars1.png'
    image_path4 = './images/dafi/23.jpeg' # PC-Path
    detect_plate(image_path4)
    
    cv2.waitKey()


main()


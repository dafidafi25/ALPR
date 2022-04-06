from turtle import width
import preprocess as pp
import cv2
import imutils as im
import numpy as np
from skimage.segmentation import clear_border

def detect_plate(input):
    img = cv2.imread(input)

    resize = im.resize(img, width=500)

    imgGrayscale, img_thresh = pp.preprocess(resize)

    cnts = cv2.findContours(img_thresh, cv2.RETR_LIST,
                                              cv2.CHAIN_APPROX_SIMPLE)  # find all contours
    cnts = im.grab_contours(cnts)

    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    detectedAr = DetectByAR(imgGrayscale,contours=cnts)
    print(detectedAr)

    if detectedAr[0][0] != None:
        cv2.imshow("ROI",detectedAr)
    else:
        DetectedByMorphological(imgGrayscale,img_thresh,resize)


def DetectByAR(imgGrayscale,contours):
    for c in contours:
        lpCnt = None
        roi = None
        valid=False
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)
        clearBorder = False
        # check to see if the aspect ratio is rectangular
        if ar >= 3 and ar <= 5:
            # store the license plate contour and extract the
            # license plate from the grayscale image and then
            # threshold it
            lpCnt = c
            licensePlate = imgGrayscale[y:y + h, x:x + w]
            roi = cv2.threshold(licensePlate, 0, 255,
                cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

            # check to see if we should clear any foreground
            # pixels touching the border of the image
            # (which typically, not but always, indicates noise)
            if clearBorder:
                roi = clear_border(roi)
            # display any debugging information and then break
            # from the loop early since we have found the license
            # plate region
            cv2.imshow("ROI",roi)
            return(roi)
    return([[None]])

def DetectedByMorphological(gray,thresh,img):
    cv2.imshow("Threshold Image",thresh)

    edged = cv2.Canny(thresh, 150 , 200)
    cv2.imshow("Edge image",edged)
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                              cv2.CHAIN_APPROX_NONE)  # find all contours
    cnts = im.grab_contours(cnts)
    blank = np.zeros(img.shape, dtype='uint8')
    temp_cnts = []
    for cnt in cnts:
        cont_area = cv2.contourArea(cnt)
        valid = False
        if(cont_area > 80 and cont_area<270):
            x,y,w,h = cv2.boundingRect(cnt)
            width = x+w
            height = y+h

            print("width : " + str(width))
            print("height : " + str(height))
            print("=====next======")
            if(width>180 and width <320  and height > 150 and height<250):
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                valid = True
                temp_cnts.append(cnt)
        # if valid and cv2.isContourConvex(cnt):
        #     temp_cnts.append(cnt)
        
    
    # cv2.drawContours(img, temp_cnts, -1, (0,255,0),cv2.CHAIN_APPROX_NONE)

    cv2.imshow("test",img)


    






def main():
    image_path4 = '/Users/dafigumawangpriadi/work/joki_ta/ALPR/images/dafi/22.jpeg'
    detect_plate(image_path4)
    cv2.waitKey()


main()


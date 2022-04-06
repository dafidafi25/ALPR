import preprocess as pp
import cv2
import imutils as im
import numpy as np
from skimage.segmentation import clear_border

def detect_plate(input):
    img = cv2.imread(input)

    resize = im.resize(img, width=500)

    imgGrayscale, img_thresh = pp.preprocess(resize)

    cv2.imshow("threshold", img_thresh)
    cv2.imshow("gray scale", imgGrayscale)

    cnts = cv2.findContours(img_thresh.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
   

    cnts = im.grab_contours(cnts)
    cv2.drawContours(resize, cnts, -1, (0,255,0), 1)
    cv2.imshow("all cntr",resize)
   
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
    

    for c in cnts:
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
            cv2.imshow("License Plate", licensePlate)
            cv2.imshow("ROI", roi)




    cv2.waitKey()


def main():
    
    image_path1 = 'D:/Dafi/Kerja/Joki TA/Rio/images/mobil/Cars1.png'
    image_path2 = 'D:/Dafi/Kerja/Joki TA/Rio/images/indo'
    image_path3 = 'D:/Dafi/Kerja/Joki TA/Rio/images/motor/74.jpg'
    image_path4 = 'D:/Dafi/Kerja/Joki TA/Rio/images/dafi/23.jpeg'
    detect_plate(image_path4)


main()


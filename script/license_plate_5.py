import cv2
from cv2 import CV_32F
import imutils as im
import numpy as np

opening = ""

def kernel_disk_shaped(r):
    n = r*2+1
    a, b = r, r
    y,x = np.ogrid[-a:n-a, -b:n-b]
    mask = x*x + y*y <= r*r
    mask = mask.astype(np.uint8)
    return(mask)

def detect_plate(input):
    
    #reading input
    image = cv2.imread(input)
    # Resize the image - change width to 500
    newwidth = 750
    input_image = im.resize(image, width=newwidth)
    # input_image = image
    #grayscale input
    gray = cv2.cvtColor(input_image,cv2.COLOR_BGR2GRAY)

    # applying iterative bilateral filter on gray scale image

    bilateral = cv2.bilateralFilter(gray, 15, 75, 75)
    # Save the output.
    # cv2.imshow('bilateral image.jpg', bilateral)

    #Contrast Enhancement using Adaptive Histogram Equalization
    clahe = cv2.createCLAHE(clipLimit=4, tileGridSize=(8, 8))
    equalized = clahe.apply(gray)

    # cv2.imshow('Contrast Enhancement .jpg', equalized)

    #Morphoplogical opening

    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel_disk_shaped(3),iterations=10)
    

    # cv2.imshow('Opening effect using disk', opening)   

    #substraction
    substracted_image = cv2.subtract(equalized, opening)

    cv2.imshow('Substacted Image', substracted_image)  

    #Image Binarization
    ret, binarization = cv2.threshold(substracted_image,255,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('binarization Image', binarization)  
    # print(ret)

    # Sobel Edge Detection

    # edged = cv2.Canny(binarization, 30, 200) 
    # cv2.imshow('edged Image', edged)  


    # kernel = np.ones((2,2), np.uint8)
    # img_dilation = cv2.dilate(edged, kernel, iterations=1)

    # cv2.imshow('Dilation image', img_dilation)

    # contours, hierarchy = cv2.findContours(img_dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # drawing = np.zeros((img_dilation.shape[0], img_dilation.shape[1], 3), dtype=np.uint8)
    # for i in range(len(contours)):
    #     cv2.drawContours(drawing, contours, i, (0,255,0), 2, cv2.LINE_8, hierarchy, 0)
    # # Show in a window
    # cv2.imshow('Contours', drawing)


    # h, w = binarization.shape[:2]
    # mask = np.zeros((h+2, w+2), np.uint8)
    # cv2.floodFill(binarization, mask, (0,0), 255)
    # im_floodfill_inv = cv2.bitwise_not(binarization)
    # im_out = binarization | im_floodfill_inv


    # im_floodfill = img_dilation

    # h, w = im_floodfill.shape[:2]
    # mask = np.zeros((h+2, w+2), np.uint8)

    # cv2.floodFill(im_floodfill, mask, (0,0), 255)
    # im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    # im_out = img_dilation | im_floodfill_inv
    # cv2.imshow("Foreground", im_out)



    cv2.waitKey(0)





import cv2
from cv2 import CV_32F
import imutils as im
import numpy as np
import math

debug = True

def detect_plate(input,minAR,maxAr,keep=5):
    ##locating candidate

    #reading input
    image = cv2.imread(input)

    #grayscale input
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #processing input
    rectKern = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
    blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKern)
    if debug == True:
        cv2.imshow('blackhat',blackhat)
    
    squareKern = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    light = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, squareKern)
    light = cv2.threshold(light, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    if debug == True: 
        cv2.imshow("Light Regions", light)
    

    gradX = cv2.Sobel(blackhat, ddepth=cv2.CV_32F,
        dx=1, dy=0, ksize=-1)
    gradX = np.absolute(gradX)
    (minVal, maxVal) = (np.min(gradX), np.max(gradX))
    gradX = 255 * ((gradX - minVal) / (maxVal - minVal))
    gradX = gradX.astype("uint8")
    if debug == True: 
        cv2.imshow("Scharr", gradX)


    gradX = cv2.GaussianBlur(gradX, (5, 5), 0)
    gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKern)
    thresh = cv2.threshold(gradX, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    if debug == True: 
        cv2.imshow("Grad Thresh", thresh)


    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    if debug == True: 
        cv2.imshow("Grad Erode/Dilate", thresh)


    thresh = cv2.bitwise_and(thresh, thresh, mask=light)
    thresh = cv2.dilate(thresh, None, iterations=2)
    thresh = cv2.erode(thresh, None, iterations=1)
    if debug == True: 
        cv2.imshow("Final", thresh)

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
    cnts = im.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:keep]
    cv2.drawContours(image, cnts, -1, (255,0,0), 2)
    cv2.imshow('All Contours', image)
    
    cv2.waitKey(0)
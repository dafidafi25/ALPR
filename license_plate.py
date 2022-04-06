import cv2
import imutils as im
import numpy as np
import math

def detect_plate(input):
    
    print(input)
    #Reading image using cv2
    input_image = cv2.imread(input)
    


    # Resize the image - change width to 500
    # newwidth = 500
    # input_image = im.resize(input_image, width=newwidth)
    image = input_image
    # RGB to Gray scale conversion
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Noise removal with iterative bilateral filter(removes noise while preserving edges)
    d, sigmaColor, sigmaSpace = 11,17,17
    filtered_img = cv2.bilateralFilter(gray, d, sigmaColor, sigmaSpace)

    # # Perform filter
    filtered_img = cv2.dilate(filtered_img, None, iterations=2)

    # Find Edges of the grayscale image
    lower, upper = 200, 250
    edged = cv2.Canny(filtered_img, lower, upper)
   

    # Find contours based on Edges
    cnts,hir = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    print("Number of Contours found : " + str(len(cnts)))
    # cv2.drawContours(image, cnts, -1, (255,0,0), 2)
    # cv2.imshow('All Contours', image)
    # cv2.imshow('Edged Image', edged)
    # cv2.imshow('Filtered Image', filtered_img)
    # cv2.imshow('gray Image', gray)

    # #try to find straigth line 
    # cdst = cv2.cvtColor(edged.copy(), cv2.COLOR_GRAY2BGR)
    # cdstP = np.copy(cdst)

    # lines = cv2.HoughLines(edged.copy(), 1, np.pi / 180, 150, None, 0, 0)
    # if lines is not None:
    #     for i in range(0, len(lines)):
    #         rho = lines[i][0][0]
    #         theta = lines[i][0][1]
    #         a = math.cos(theta)
    #         b = math.sin(theta)
    #         x0 = a * rho
    #         y0 = b * rho
    #         pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
    #         pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
    #         cv2.line(cdst, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
    
    
    # linesP = cv2.HoughLinesP(edged.copy(), 1, np.pi / 180, 50, None, 50, 10)
    
    # if linesP is not None:
    #     for i in range(0, len(linesP)):
    #         l = linesP[i][0]
    #         cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)
    
    # cv2.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
    # cv2.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
    

    # finding 4 corners
    cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:10]

    NumberPlateCnt = None
  

    # loop over our contours to find the best possible approximate contour of number plate
    count = 0
    for c in cnts:
            peri = cv2.arcLength(c, True)
            
            epsilon = 0.01 * peri
            approx = cv2.approxPolyDP(c, epsilon, True)
            if len(approx) == 4:  # Select the contour with 4 corners
                print(approx)
                NumberPlateCnt = approx #This is our approx Number Plate Contour
                break




    # Display the original image
    cv2.imshow("Input Image", input_image)
    # Display Grayscale image
    cv2.imshow("Gray scale Image", gray)
    # Display Filtered image
    cv2.imshow("After Applying Bilateral Filter", filtered_img)
    # Display Canny Image
    cv2.imshow("After Canny Edges", edged)
    # Drawing the selected contour on the original image
    try :
        cv2.drawContours(image, [NumberPlateCnt], -1, (255,255,0), 2)
        cv2.imshow("Output", image)
    except :
        print("Plate number not found")

    cv2.waitKey(0) #Wait for user input before closing the images displayed
import cv2
import argparse
import os
import shutil
import numpy as np
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

'''
this function convert image into matrix of image rows
'''
def imgToMatrixR(img):
    # get dimensions
    height, width = img.shape
    matrix = []
    # getting pixels values for all rows
    for i in range(0, height):
        row = []
        for j in range(0, width):
            row.append(img[i,j])
        matrix.append(row)
    return matrix
'''
this function convert image into matrix of image columns
'''
def imgToMatrixC(img):
    # get dimensions
    height, width = img.shape
    matrix = []
    # getting pixels values for all columns
    for i in range(0, width):
        col = []
        for j in range(0, height):
            col.append(img[j, i])
        matrix.append(col)
    return matrix
'''
this function count a specific value (parameter p) in matrix
'''
def countPixel(matrix,p):
    counter = []
    for k in range(0, len(matrix)):
        counter.append(matrix[k].count(p))
    return counter
'''
this function searches for underlines  and replace the pixels that formed it with white pixels 
'''
def removeUnderline(binary):
    min_length=60
    matrix = imgToMatrixR(binary)
    for i in range(0, len(matrix)):
        row=matrix[i]
        start=-1
        end=0
        conn=0
        for j in range(0, len(row)):
            if (row[j]==0):
                conn=conn+1
                # first point in the line .
                if( start == -1 ):
                    start=j
                # last point in the row .
                if( j == len(row)-1 ):
                    end =j
                    if (conn >min_length):
                        binary[i:i+1, start:end+1] = 255
                    start = -1
                    end = 0
                    conn=0
            # end of the line
            else:
                end =j
                if (conn >min_length):
                    binary[i-1:i+3,start:end+1]=255
                start=-1
                end=0
                conn=0
'''
this function clears all horizontal boundaries around the input image
'''
def clearBounds_horiz(img):
    height, width = img.shape
    matrix = imgToMatrixR(img)
    white_counter = countPixel(matrix,255)

    for i in range (0,height):
        if(white_counter[i]>= width-1):
            img = img[1:height,0:width]
        else:
            break

    new_height, width = img.shape
    for i in range (1,height):
        if(white_counter[height-i]>= width-1):
            img = img[0:new_height-i,0:width]
        else:
            break

    return img
'''
this function clears all vertical boundaries around the input image
'''
def clearBounds_vert(img):
    height, width = img.shape
    matrix = imgToMatrixC(img)
    white_counter = countPixel(matrix,255)

    for i in range (0,width):
        if(white_counter[i]>= height-1):
            img = img[0:height,1:width]
        else:
            break

    height, new_width = img.shape
    for i in range (1,width):
        if(white_counter[width-i]>= height-1):
            img = img[0:height,0:new_width-i]
        else:
            break

    return img

'''
this function applies a set of preprocessing operations to the input image, function output is a binarized image.
operations are scaling , grayscaling , noise clearing , gaussian's thresholding and remove underlines.
finally the function calls lineSegment function to segment the image into lines.
'''
def pre_processing(path):
    # Read Image
    img = cv2.imread(path)

    # scaling
    height, width = img.shape[:2]
    if (height < 1600 and width < 1200):
       scaled = cv2.resize(img, (2 * width, 2* height), interpolation=cv2.INTER_LINEAR)
    # cv2.imwrite('(0)Scale.jpg', scaled)

    # Grayscale step
    grayscaled = cv2.cvtColor(scaled, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite("(2)grayscale.jpg", grayscaled)

    # Noise Clearing step
    noise_cleared = cv2.fastNlMeansDenoising(grayscaled, None, 4, 7, 21)
    # cv2.imwrite("(3)denoise.jpg", noise_cleared)

    '''
    # GAUSSIAN's thresholding
    GBinary = cv2.adaptiveThreshold(noise_cleared,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,5)
    # cv2.imwrite("(4)binarization.jpg", GBinary)
    '''

    # Otsu's thresholding after Gaussian filtering
    blur = cv2.GaussianBlur(noise_cleared, (5, 5), 0)
    ret3, OBinary = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # cv2.imwrite("(4)binarization.jpg", OBinary)

    # Remove underlines
    # removeUnderline(OBinary)
    # cv2.imwrite("(5)underlined.png", GBinary)

    cv2.imwrite("Preprocessing.png", OBinary)

    if os.path.exists("..\..\output\segmentation"):
        shutil.rmtree("..\..\output\segmentation")
    line_segment(OBinary)

'''
this function segment the binarized image into lines
segmentation technique consists of 3 steps :
    1- define potential segmentation rows that contains no or 20 black pixels at most.
    2- filter the potential segmentation rows and determine only segmentation rows which the crop operation depends on.
    3- segment the image into lines.
'''
def line_segment(binary):
    #get dimentions
    height, width = binary.shape
    #convert image into matrix of rows
    matrix = imgToMatrixR(binary)
    #count black pixels in each row
    black_counter =countPixel(matrix,0)

    # determine potential segmentation rows (psr)
    # psr is any row contains 0-20 black pixels, last row in image is also a psr .
    psr=[0]
    for i in range(0, len(black_counter)):
        if (black_counter[i] <= 20 or i >= len(black_counter) - 2):
            psr.append(i)

    # determine segmentation rows sr
    # sr is the index where we segment the image
    sr = []
    count=0
    for n in range(0, len(psr) - 1):
        # combine each set of sequence white rows into only one sr
        if (psr[n] + 3 < psr[n + 1] or n >= len(psr) - 2):
            sr.append(psr[n - int(count/2)])
            count=0
        else:
            count += 1

    # segment image into lines
    for c in range(0, len(sr) - 1):
        crop_img = binary[sr[c]:sr[c + 1],0:width ]
        crop_img = clearBounds_horiz(crop_img)
        crop_img = clearBounds_vert(crop_img)
        os.makedirs("..\..\output\segmentation\line "+str(c))
        # cv2.imwrite("..\..\output\segmentation\line "+str(c)+"\\line " + str(c) + ".png", crop_img)
        # Call function to Segment the line into words then chars
        word_segment(crop_img,"column",c,None)

'''
this function segment lines into columns then words
lineNum and columnNum parameters used for naming, flag parameter refers to the type of segmentation.
segmentation technique consists of 4 steps :
    1- define potential segmentation columns that contains no or only two black pixels.
    2- filter the potential segmentation columns,determine only segmentation columns which the crop operation depends on
    3- segment the image into segments (column)
    4- recursive call to segment columns into words
'''
def word_segment(binary,flag,lineNum,columnNum):

    column_threshold=120
    word_threshold=13

    #get image dimension
    height, width = binary.shape
    #convert image to matrix of columns
    matrix = imgToMatrixC(binary)
    #count black pixels in each column
    black_counter = countPixel(matrix,0)

    # determine potential segmentation columns (psc).
    # psc is any column contains no or two black bixel at most , last column in image is also a psc .
    psc = [0]
    for p in range(0, len(black_counter)):
        if (black_counter[p] <= 2 or p >= len(black_counter) - 2):
            psc.append(p)

    # determine segmentation columns (sc)
    # sc is the index where we segment the image .
    sc = []
    count = 0
    for n in range(0, len(psc) - 1):
        # first column is sc
        if (n ==0):
            sc.append(psc[n])
            count = 0
        # last column is also sc
        elif (n >= len(psc) - 2):
            sc.append(psc[n])
            count = 0

        # combine each set of sequence white columns into only one sc
        elif (psc[n] + 3 < psc[n + 1] ):
            # space between columns >= threshold value, low values is a space between words/chars not words.
            if (flag=="column"):
                if (count > column_threshold):
                    sc.append(psc[n -int(count/2)])
                count = 0
            if (flag=="word"):
                if (count >= word_threshold ):
                    sc.append(psc[n -int(count/2)])
                count = 0

        else :
            count += 1
    if(flag=="column"):
        for c in range(0, len(sc) - 1):
                crop_img = binary[0:height, sc[c]:sc[c + 1]+2]
                crop_img = clearBounds_vert(crop_img)
                directory = "..\..\output\segmentation\line " + str(lineNum) + "\\column "+str(c)
                os.makedirs(directory)
                # cv2.imwrite(directory + "\\column " + str(c) + ".png", crop_img)
                word_segment(crop_img,"word",lineNum,c)

    if (flag == "word"):
        for c in range(0, len(sc) - 1):
            crop_img = binary[0:height, sc[c]:sc[c + 1] + 2]
            directory = "..\..\output\segmentation\line " + str(lineNum) + "\\column " + str(columnNum)+"\\word " + str(c)
            os.makedirs(directory)
            # cv2.imwrite(directory + "\\word " + str(c) + ".png", crop_img)
            char_segment(crop_img, lineNum, columnNum, c)


'''
this function segment words into chars
lineNum,colNum and wordNum parameters used for naming 
segmentation technique consists of 3 steps :
    1- define potential segmentation columns that contains no or only one black pixels.
    2- filter potential segmentation columns by determine segmentation columns which the crop operation depends on .
    3- segment the image into segments (chars).
'''
def char_segment(binary,lineNum,colNum,wordNum):

    # get image dimension
    height, width = binary.shape
    # convert image to matrix of columns
    matrix = imgToMatrixC(binary)
    # count black pixels in each column
    black_counter = countPixel(matrix,0)

    # determine potential segmentation columns (psc).
    # psc is any column contains no or one black bixel at most , last column in image is also a psc .
    psc = [0]
    for p in range(0, len(black_counter)):
        if (black_counter[p] <= 1 or p >= len(black_counter) - 2):
            psc.append(p)

    # determine segmentation columns (sc)
    # sc is the average column between each sequence set of psc , average = summ of columns index/count of columns
    sc = []
    summ = 0
    count = 0
    for n in range(0, len(psc) - 1):
        summ = summ + psc[n]
        count = count + 1
        # combine each set of sequence white columns into only one sc ,last column is also a sc
        if (psc[n] + 3 < psc[n + 1] or n >= len(psc) - 2):
            sc.append(int(summ / count))
            summ = 0
            count = 0

    # segment image into chars
    for c in range(0, len(sc) - 1):
        crop_img = binary[0:height, sc[c]:sc[c + 1]+2]
        crop_img = clearBounds_horiz(crop_img)
        crop_img = clearBounds_vert(crop_img)
        crop_img = cv2.resize(crop_img, (64, 128), interpolation=cv2.INTER_LINEAR)
        directory= "..\..\output\segmentation\line " + str(lineNum)+"\\column "+str(colNum)+"\\word "+str(wordNum)
        if not os.path.exists(directory):
            os.makedirs(directory)
        cv2.imwrite(directory+"\\"+str(c)+".png", crop_img)

# Preprocessing function Calling
#pre_processing("testCases\\1.png")
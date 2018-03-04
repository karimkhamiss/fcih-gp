import os
import pandas as pd
import cv2
import numpy as np
import csv
import shutil
from sklearn.externals import joblib

#create histogram for each letter that has been segmented from the paper
from core.hog.HOG_Imp import Hogfun
from core.preprocessing.PrePlusSeg import pre_processing
from core.postprocessing.postproccessing import match

def output_his():
    vectorList = []  #list for both cols after recognation so it carry vectors
    list_cols = pre_processing("..\..\\resources\\testcases\\test.jpg")
    # loop for cols
    for list_col in list_cols:
        vector_list = []
        for line in list_col:
            List = []
            for image in line:
                if type(image) is str:   # case of ","
                    List.append(",")
                    continue
                else:
                    imagevector=Hogfun(image, (8, 8), (2, 2))
                    List.append(imagevector)
            vector_list.append(List)
        vectorList.append(vector_list)
    return vectorList


def prediction(List):
    word = ''      # to concatentate char of each word
    wordList = ''  # to concatentate words in the same line
    lineList = []  # list of lines that each line contain list of words
    linetype = []  # datatype of each line in col2

    for vector_list in List:  # vector_list1 =>col1 , vector_list2 =>col2
        index = 0
        for line in vector_list:  # new line and new word
            index += 1
            if linetype:
                if linetype[index] == "letters":
                    clf = joblib.load('../models/letters.pkl')
                elif linetype[index] == "digits":
                    clf = joblib.load('../models/digits.pkl')
            else:
                clf = joblib.load('../models/letters.pkl')
            for vector in line:
                if type(vector) is str :  # in the same line but not in the same word ","
                    print("word is ", word)
                    wordList += word
                    word = ' '
                else:  # in the same line and the same word
                    predict = clf.predict([vector])
                    word += predict[0]

            # new line and new word
            print("word is ", word)
            wordList += word
            lineList.append(wordList)
            wordList = ''
        linetype=match(lineList)       #send all prediction to col1 return type of each line in col2

    return lineList


#calling
List = []
List = output_his()
linelist= prediction(List)



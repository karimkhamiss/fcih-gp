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


def output_his():
    '''
    list_col1 = [['a', 'y', 'a', ',', 'a', 'l', 'i',','],
                 ['H', 'e', 'n', 'd', ',', 'a', 'h', 'm', 'e', 'd',',']]  # assumtion return from preproccessing col1
    list_col2 = [['a', 'l', 'i', ',', 's', 'a', 'm', 'a', 'h',','],
                 ['H', 'e', 'b', 'a', ',', 'H', 'o', 's', 'a', 'm',',']]  # assumtion return from preproccessing col2
    list_cols = [list_col1, list_col2]  # assumtion return from preproccessing
    '''
    vectorList = []  #list for both cols after recognation so it carry vectors
    list_cols = pre_processing("..\..\\resources\\testcases\\test.jpg")
    # loop for cols
    for list_col in list_cols:
        vector_list = []
        for line in list_col:
            List = []
            for image in line:
                if image == ",":
                    List.append(",")
                    continue
                else:
                    print(image)
                    imagevector=Hogfun(image, (8, 8), (2, 2))
                    print("image vector len", len(imagevector))
                    #imagevector = ['0', '1', '0']  # assumtion
                    List.append(imagevector)
            vector_list.append(List)
        vectorList.append(vector_list)
    return vectorList


def prediction(List):
    word = ''  # to concatentate char of each word
    wordList = ''  # to concatentate words in the same line
    lineList = []  # list of lines that each line contain list of words

    linetype = []  # hend return in

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
                if vector == ',':  # in the same line but not in the same word
                    print("word is ", word)
                    wordList += word
                    word = ' '
                else:  # in the same line and the same word
                    predict = clf.predict(vector)
                    # print("pediction ", predict[0])
                    word += predict[0]

            # new line and new word
            print("word is ", word)
            wordList += word
            lineList.append(wordList)
            wordList = ''
        # linetype=hend(lineList)       #send all prediction to col1 return type of each line in col2

    return lineList


#calling
List = []
List = output_his()
# prediction(List)
for vector_list in List:
    for line in vector_list:
            print(line)


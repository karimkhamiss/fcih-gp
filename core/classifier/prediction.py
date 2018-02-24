import os
import pandas as pd
import cv2
import numpy as np
import csv
import shutil
from sklearn.externals import joblib

#create histogram for each letter that has been segmented from the paper put in outputHis folder
from core.hog.HOG_Imp import Hogfun
from core.preprocessing.PrePlusSeg import pre_processing

def output_his():
    if os.path.exists("..\..\output\histograms\input"):
        shutil.rmtree("..\..\output\histograms\input")
        os.mkdir("..\..\output\histograms\input")
    else:
        os.mkdir("..\..\output\histograms\input")
    output_list = [x[0] for x in os.walk("..\..\output\segmentation")]  # walk to that path
    for each_dir in output_list[1:]:  # line 0 ,line 1 , line 3
        if ("word" in each_dir):
            files = os.listdir(each_dir)  #0.png,1.png
            index =0
            for file  in files: #0.png
                path =each_dir+'\\'+file   #each char path
                print('path ', path)
                df = pd.DataFrame(columns=range(0, 3780))
                curr_line = path.split("\\")[4]
                curr_col = path.split("\\")[5]
                curr_word = path.split("\\")[6]
                curr_file = path.split("\\")[7]
                #save in and as
                fileName="..\..\output\histograms\input\\"+curr_line+"-"+curr_col+"-"+curr_word+"-"+curr_file   #name of csv file for each character
                index+=1
                image= cv2.imread(path,0)
                height, width = image.shape[:2]
                print('height',height)
                print('width', width)
                #calculate angle & magnitude
                imagevector = Hogfun(image, (8, 8), (2, 2))
                print("image vector len", len(imagevector))
                # write in csv file
                try:
                    df.loc[len(df)] = imagevector
                except Exception as e:
                    pass
                save = fileName + ('.csv')
                #print(save)
                df.to_csv(save)  # save as csv file


def prediction():
    flag=True      #for the first file that have no prev
    prevfile=''
    word=''         #to concatentate char of each word
    wordList=''      #to concatentate words in the same line
    lineList=[]     #list of lines that each line contain list of words
    files = os.listdir("..\..\output\\histograms\\input")
    for file in files:   #each csv file in outputHis

        clf = joblib.load('../models/digits_letters.pkl')
        '''
        #to know which one of the two models to use
        if file.split('-')[1]=="column 0":               #left side
            clf = joblib.load('../models/letters.pkl')
        elif file.split('-')[1]=="column 1":     #right side
            clf = joblib.load('../models/digits.pkl')#how do i know
        '''

        with open('..\..\output\\histograms\\input\\'+file) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')   #read data
            mark=True             #became true when read new csv file
            for row in readCSV:
                if mark==True:   #to skip first row in csv file
                    mark=False
                    continue
                else:
                    predict = clf.predict(np.array([row[1:]]))
                    #print("pediction ", predict[0])
                    if flag:       # for the first file that have no prev
                        word +=predict[0]
                        flag = False
                    else:
                        print('prev file ', prevfile)
                        print('curr file', file)
                        if prevfile.split('-')[0]==file.split('-')[0]:      #check if in the same line
                            if prevfile.split('-')[2]==file.split('-')[2]: #check if in the same word
                                word+=predict[0]       #in the same line and the same word
                            else:  #in the same line but not in the same word
                                print("word is ",word)
                                wordList +=word
                                word=predict[0]

                        else:         #not in the same line   #not in the same word
                            print("word is ", word)
                            wordList +=' '+word
                            lineList.append(wordList)
                            wordList=''
                            word=predict[0]
        prevfile=file
    wordList +=' '+word
    lineList.append(wordList)
    return lineList





#calling
pre_processing("..\..\\resources\\testcases\\test.jpg")
output_his()
lineList=prediction()
for line in lineList:
    print (line)




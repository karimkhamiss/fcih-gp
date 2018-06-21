from sklearn.externals import joblib
#from skimage.feature import hog
import cv2


#create histogram for each letter that has been segmented from the paper
from core.hog.HOG_Imp import Hogfun
from core.preprocessing.PrePlusSeg import pre_processing
from core.postprocessing.postproccessing import match
from core.postprocessing.finalResult import getTestResult

def output_his():
    vectorList = []  #list for both cols after recognation so it carry vectors
    list_cols = pre_processing("..\..\\resources\\testcases\\tes2.jpg")
    print("start")
    counter=0
    #hog start
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
                    counter+=1
                    cv2.imwrite("..\..\\resources\\images\\"+"img"+str(counter)+".jpg",image)
                    imagevector=Hogfun(image, (8, 8), (2, 2)) #hog we have build
                    #imagevector=hog(image, orientations=8, pixels_per_cell=(8,8),cells_per_block=(2, 2), visualise=False)   #build in function
                    List.append(imagevector)
            vector_list.append(List)
        vectorList.append(vector_list)
    print("end") #hog end
    list_cols=[]
    return vectorList

def prediction(List):
    word = ''      # to concatentate char of each word
    wordList = ''  # to concatentate words in the same line
    lineList = []  # list of lines that each line contain list of words
    linetype = []  # datatype of each line in col2
    colList=[]
    flag=True
    flag2=True
    for vector_list in List:  # vector_list1 =>col1 , vector_list2 =>col2
        index = 0
        for line in vector_list:  # new line and new word
            if flag2==False:
                flag2=True
                continue
            if linetype:
                if linetype[index] == 'letter':
                    clf = joblib.load('../models/letters.pkl')
                    index += 1
                elif linetype[index] == 'digit':
                    clf = joblib.load('../models/digits.pkl')
                    index += 1
                elif linetype[index]=='none':
                    lineList.append('none')
                    index += 1
                    continue
            else:
                clf = joblib.load('../models/letters.pkl')
            for vector in line:
                if type(vector) is str :  # in the same line but not in the same word ","
                   # print("word is ", word)
                    wordList += word
                    word = ' '
                else:  # in the same line and the same word
                    predict = clf.predict([vector])
                    word += predict[0]

            # new line and new word
            wordList += word
            lineList.append(wordList)
            wordList = ''

        print("col after recognation >>",lineList)
        if flag:
            linetype=match(lineList)       #send all prediction to col1 return type of each line in col2
            print("match return >>",linetype)
            flag=False                   #to git in only once
            flag2=False
        print("col after postproccessing >>", lineList)
        colList.append(lineList)
        colList.append(linetype[-1])#will be deleted
        lineList=[]

    return colList[:-1]                      #will be deleted



#calling
#List = []
#List = output_his()   #return list of vectors in  each image but in list
#linelist= prediction(List)
#print("linnnnnnnnnne ", getTestResult(linelist,12,"male"))
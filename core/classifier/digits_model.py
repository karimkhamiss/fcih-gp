import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, cross_validation, neighbors
import pandas as pd
import csv
from sklearn.externals import joblib


#using csv classifier
targetList=['0','1','2','3','4','5','6','7','8','9']

#targetList=['0','1','2','3','4','5','6','7','8','9']


def build_Classifier_Digits():
    features  = []         #features which is histograms values
    corresponding= []      #coresponding target to that feature

    clf = svm.SVC(kernel='linear', C=1.0)  # classifier

    for target in targetList:     #for loop for Digits targets
        counter = 0.0
        with open('..\..\output\histograms\dataset\digits\\'+'HOGD_'+target+'.csv') as csvfile:
            row_count = len(open('..\..\output\histograms\dataset\digits\\'+'HOGD_' + target + '.csv').readlines()) #number of rows per csv(number of samples)
            #print row_count
            #print "traingU ",row_count*0.67
            readCSV = csv.reader(csvfile, delimiter=',')  #read data
            counter+=1
            for row in readCSV:          #each row in csv file
                if counter==1:
                    counter+=1
                    pass
                else:
                    counter+=1
                    if counter>=row_count*0.67:  #to use only 2/3 from samples in triaing
                        #print counter
                        break
                    # add features to features list
                    features.append(row[1:])  #this 1 to skip first coloum which is line number
                    # add corresponding target to that feature in corresponding list
                    corresponding.append(target)



    X=np.array(features)       #features
    y=np.array(corresponding)  #corresponding target

    print ('traning samples >>', len(X))
    # print 'traning samples >>',len(y)
    clf.fit(X,y)       #traning

    joblib.dump(clf, '..\models\digits.pkl', compress=3)  # build classifier Model



def test_classifier_Digits():
    features = []  # features which is histograms values
    corresponding = []  # coresponding target to that feature

    # load classifier model
    clf = joblib.load('..\models\digits.pkl')
    for target in targetList:
        counter = 0
        with open('..\..\output\histograms\dataset\digits\\'+'HOGD_'+target+'.csv') as csvfile:
            row_count = len(open('..\..\output\histograms\dataset\digits\\'+'HOGD_' + target + '.csv').readlines()) #number of rows per csv(number of samples)
            print (target)
            readCSV = csv.reader(csvfile, delimiter=',')     #Read data
            counter+=1
            for row in readCSV:         #each row in csv file
                counter+=1
                if counter <= row_count*0.67:
                    pass
                else:
                    features.append(row[1:])  # this 1 to skip first coloum which is line number
                    corresponding.append(target)  # add corresponding target to that feature in corresponding list
                    #print counter
                    #print row[1:]
                    print ('Predict :',clf.predict(np.array([row[1:]]))) #testing


    X = np.array(features)  # features
    y = np.array(corresponding)  # corresponding target
    #print 'traning samples >>',len(X)
    accuracy = clf.score(X, y)
    print ('accuraccy >>',accuracy)


# build_Classifier_Digits()

#test_classifier_Digits()

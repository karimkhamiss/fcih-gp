import  pandas as pd
import os
import cv2
# i use main function to create histograms file which is exist in histograms folder now
# i use dataset exist in training folder
from core.hog.HOG_Imp import Hogfun


def HOG():
    upperpath = "..\..\\resources\dataset\\upper"  # path of dataset -letters in upper case
    lowerpath = "..\..\\resources\dataset\\lower"  # path of dataset -letters in lower case
    digitpath = "..\..\\resources\dataset\digits"  # path of dataset digits
    pathList =[digitpath]   #list to all datalists folders
    for path in pathList:
        stock_list = [x[0] for x in os.walk(path)]  #walk to that path
        for each_dir in stock_list[1:]:  #acces each dir in that path  ex A ,B ,C ...
                each_file = os.listdir(each_dir)  # list of all files in dir A
                ticker = each_dir.split("\\")[5]  #extract the file name of each target ex A,B,C
                print (ticker)
                #path for saving histograms files in
                # if path ==upperpath:
                #     gather = "..\..\output\histograms\dataset\Letters\HOGU_" + ticker  #upper
                # if path == lowerpath:
                #     gather = "..\..\output\histograms\dataset\Letters\HOGL_" + ticker  #lower
                if path == digitpath:
                    gather="..\..\output\histograms\dataset\Digits\HOGD_" + ticker    #digits


                counter = 0
                df = pd.DataFrame(columns=range(0, 3780))
                if len(each_file) > 0:  # check if dir is not empty
                    for file in each_file:  # each file in each dir ex 0.png ,1.png ,...
                        # print (counter,each_dir + '\\' + file)
                        counter += 1
                        img = cv2.imread((each_dir + '\\' + file), 0)

                        # histogram -return one histogram for each image
                        imagevector = Hogfun(img, (8, 8), (2, 2))
                        print ("image vector len", len(imagevector))
                        try:
                            df.loc[len(df)] = imagevector
                            # df = df.append(fd, ignore_index=True)
                            print ("OK")
                        except Exception as e:
                            pass

                        save = gather + ('.csv')
                        print(save)
                        df.to_csv(save)  # save as csv file


# function Calling
if __name__== "__main__":
    HOG()
    # build_Classifier_Digits()
    # build_Classifier_Letters()
    # build_Classifier_OneModel()
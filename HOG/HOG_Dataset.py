import cv2
import  pandas as pd
import os

from HOG.HOG_Imp import Hogfun


#Used To Calculate Hog Of All Dataset

list_hog_fd = []
def Upper():
    path = "dataset\\upper"  # path of dataset -letters in upper case
    stock_list = [x[0] for x in os.walk(path)]  # walk to that path
    for each_dir in stock_list[1:]:  # acces each dir in that path  ex A ,B ,C ...
        each_file = os.listdir(each_dir)  # list of all files in dir A
        ticker = each_dir.split("\\")[2]  # extract the file name of each target ex A,B,C
        # path for saving histograms files in
        gather = "Histograms_Letters\HOGU_" + ticker  # upper

        df = pd.DataFrame(columns=range(0, 3780))
        if len(each_file) > 0:  # check if dir is not empty
            for file in each_file:  # each file in each dir ex 0.png ,1.png ,...
                print (each_dir + '\\' + file)
                # preproccesing sample i mean image
                #scaledGBinary = pre_processing(each_dir + '\\' + file)

                img = cv2.imread((each_dir + '\\' + file),0)

                # histogram -return one histogram for each image
                imagevector = Hogfun(img, (8, 8), (2, 2))
                print ("image vector len", len(imagevector))
                try:
                    df.loc[len(df)] = imagevector
                    #df = df.append(fd, ignore_index=True)
                    print("OK")
                except Exception as e:
                    pass

                save = gather + ('.csv')
                print(save)
                df.to_csv(save)  # save as csv file


def Lower():
    path = "dataset\lower"  #path of dataset -letters in lower case
    stock_list = [x[0] for x in os.walk(path)]  # walk to that path
    for each_dir in stock_list[1:]:  # acces each dir in that path  ex A ,B ,C ...
        each_file = os.listdir(each_dir)  # list of all files in dir A
        ticker = each_dir.split("\\")[2]  # extract the file name of each target ex A,B,C
        # path for saving histograms files in
        gather = "Histograms_Letters\HOGL_" + ticker  # upper

        df = pd.DataFrame(columns=range(0, 3780))
        if len(each_file) > 0:  # check if dir is not empty
            for file in each_file:  # each file in each dir ex 0.png ,1.png ,...
                print (each_dir + '\\' + file)
                # preproccesing sample i mean image
                #scaledGBinary = pre_processing(each_dir + '\\' + file)

                img = cv2.imread((each_dir + '\\' + file),0)

                # histogram -return one histogram for each image
                imagevector = Hogfun(img, (8, 8), (2, 2))
                print ("image vector len", len(imagevector))

                try:
                    df.loc[len(df)] = imagevector
                    print ("OK")
                except Exception as e:
                    pass

                save = gather + ('.csv')
                print(save)
                df.to_csv(save)  # save as csv file

def Digit():
    path = "..\dataset\digits"  # path of dataset -letters in lower case
    stock_list = [x[0] for x in os.walk(path)]  # walk to that path
    for each_dir in stock_list[1:]:  # acces each dir in that path  ex A ,B ,C ...
        each_file = os.listdir(each_dir)  # list of all files in dir A
        ticker = each_dir.split("\\")[2]  # extract the file name of each target ex A,B,C
        # path for saving histograms files in
        gather = "Histograms_Digits\HOGD_" + ticker  # upper

        df = pd.DataFrame(columns=range(0, 3780))
        if len(each_file) > 0:  # check if dir is not empty
            for file in each_file:  # each file in each dir ex 0.png ,1.png ,...
                print (each_dir + '\\' + file)
                # preproccesing sample i mean image
                #scaledGBinary = pre_processing(each_dir + '\\' + file)

                img = cv2.imread((each_dir + '\\' + file),0)

                # histogram -return one histogram for each image
                imagevector = Hogfun(img, (8, 8), (2, 2))
                print ("image vector len", len(imagevector))

                try:
                    df.loc[len(df)] = imagevector
                    print ("OK")
                    # df = df.append(fd, ignore_index=True)
                except Exception as e:
                    pass

                save = gather + ('.csv')
                print(save)
                df.to_csv(save)  # save as csv file


# function Calling
if __name__ == "__main__":
    #Upper()
    #Lower()
    Digit()









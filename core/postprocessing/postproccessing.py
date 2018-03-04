import pickle
import difflib

class Test:
    def __init__(self,category,name,type,maleList,femaleList,decrease,increase):
        self.name = name
        self.category = category
        self.type = type
        self.male=maleList
        self.female =femaleList
        self.decrease = decrease
        self.increase = increase

    def display(self):
        print(self.increase)


startTest = []
startTest.append(Test(["Liver Diseases","Blood Diseases","Complete Blood Count","CBC","Clinical chemistry","Complete Blood Picture"],"","digit",[(0,100),(3.4,5)],[(0,100),(3.4,5)],"يقل فى حالات سوء التغذية - يقل فى حالة أمراض الكبد","لا يزيد"))

testsList = []
testsList.append(Test(["Liver Diseases"],"ALbumin","digit",[(0,100),(3.4,5)],[(0,100),(3.4,5)],"يقل فى حالات سوء التغذية - يقل فى حالة أمراض الكبد","لا يزيد"))
testsList.append(Test(["Liver Diseases"],"Aspartate Aminotransferase","digit",[(0,100),(37,100)],[(0,100),(37,100)],"لا يقل","التهاب الكبد A,B,C - فشل الكبد - الأورام - الفيروسات"))
testsList.append(Test(["Liver Diseases"],"Bil D","digit",[(0,100),(.3,100)],[(0,100),(.3,100)],"لا يقل","يزيد بسبب الصفرا و أمراض الكبد ويسبب اصفرار لون العين"))
testsList.append(Test(["Liver Diseases"],"Bilirubin, Direct","digit",[(0,100),(.3,100)],[(0,100),(.3,100)],"لا يقل","يزيد بسبب الصفرا و أمراض الكبد ويسبب اصفرار لون العين"))
testsList.append(Test(["Liver Diseases"],"Bil T","digit",[(0,100),(1.9,1.9)],[(0,100),(1.9,1.9)],"لا يقل","يزيد بسبب الصفرا و أمراض الكبد ويسبب اصفرار لون العين"))
testsList.append(Test(["Liver Diseases"],"Bilirubin, Total","digit",[(0,100),(1.9,1.9)],[(0,100),(1.9,1.9)],"لا يقل","يزيد بسبب الصفرا و أمراض الكبد ويسبب اصفرار لون العين"))



testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","Complete Blood Picture"],"D Dimer","digit",[(0,100),(1,500)],[(0,100),(1,500)],"فى حالة استئصال الغدة البار دراقية - قلة افراز الغدة الباردراقية ","التهاب الكبد A,B,C - فشل الكبد - الأورام - الفيروسات"))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","Complete Blood Picture"],"Fibrinogen","digit",[(0,100),(1,500)],[(0,100),(1,500)]," ","يزيد فى حالة الأمراض الخبيثة و أمراض الكبد "))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","Complete Blood Picture"],"PCV","digit",[(0,100),(40.7,50.3)],[(0,100),(36.1,44.3)]," يقل عند الانيميا و فقر الدم","يزيد عند زيادة نسبة الحديد فى الدم"))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","Hematocrit","Complete Blood Picture"],"Haemoglobin","digit",[(0,100),(13.5,17.5)],[(0,100),(12,15.5)],"فى حالة استئصال الغدة البار دراقية - قلة افراز الغدة الباردراقية ","التهاب الكبد A,B,C - فشل الكبد - الأورام - الفيروسات"))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC"],"Iron","digit",[(0,100),(65,175)],[(0,100),(50,170)],"يقل فى حالة الانيميا و حالات فقر الدم ","التهاب الكبد A,B,C - فشل الكبد - الأورام - الفيروسات"))




testsList.append(Test(["Clinical chemistry"],"Urea","digit",[(0,100),(6,20)],[(0,100),(6,20)],"لا يقل","عند وجود أمراض فى الكلى مثل الفشل الكلوى"))
testsList.append(Test(["Clinical chemistry"],"Uric Acid","digit",[(0,100),(4.5,8)],[(0,100),(2.5,6.2)],"لا يقل","يزيد عند مرض النقرص"))
testsList.append(Test(["Clinical chemistry"],"Creatinine","digit",[(0,100),(.7,1.3)],[(0,100),(.6,1.1)],"لا يقل","عند وجود أمراض فى الكلى مثل الفشل الكلوى"))
testsList.append(Test(["Clinical chemistry"],"GGT","digit",[(0,100),(5,85)],[(0,100),(5,85)],"لا يقل","انسداد القنوات المرارية"))
testsList.append(Test(["Clinical chemistry"],"CA","digit",[(0,100),(8.5,10.1)],[(0,100),(8.5,10.1)],"فى حالة استئصال الغدة البار دراقية - قلة افراز الغدة الباردراقية ","التهاب الكبد A,B,C - فشل الكبد - الأورام - الفيروسات"))





for test in startTest:
    for cat in test.category:
     pickle.dump(test, open(cat+".bin", "wb"))

for test in testsList:
    for cat in test.category:
      pickle.dump(test, open(cat+".bin", "ab"))



def match(lineList):
    tests = []
    lineListTypes=[]
    result=""

    filesList=["Liver Diseases","Blood Diseases"," Complete Blood Count","CBC","Clinical chemistry"]
    fileFromList = lineList[0].split(" ")


    for file in filesList:
        fileNamesplits = file.split(" ")
        if len(fileFromList)==len(fileNamesplits):

         i=0
         for fn in fileNamesplits:
            ratio = difflib.SequenceMatcher(None, fn, fileFromList[i]).ratio()

            if ratio >= 0.5:
                i += 1
                if i==len(fileFromList):
                    lineList[0]=file
                    print("file name : ",file)

            else:
             break





    with (open(lineList[0]+".bin", "rb")) as openfile: # file name will be determined by category name from the test
        while True:
            try:
                tests.append(pickle.load(openfile))

            except EOFError:
                break


    for i in range(1,len(lineList)):
        for test in tests:
            ratio = difflib.SequenceMatcher(None,test.name , lineList[i]).ratio()
            if ratio >= 0.5:
                print("matched with : " + test.name)
                lineList[i]=test.name
                lineListTypes.append(test.type)



    return lineListTypes


#types=match(["liver diseas","xcbumi"])
#print(types)




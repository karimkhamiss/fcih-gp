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
startTest.append(Test(["Liver Diseases","Blood Diseases","Complete Blood Count","CBC","Clinical chemistry","complete blood picture"],"","digit",[(0,100),(3.4,5)],[(0,100),(3.4,5)],"يقل فى حالات سوء التغذية - يقل فى حالة أمراض الكبد","لا يزيد"))
startTest.append(Test(["Clinical chemistry"],"Urea","digit",[(0,100),(6,20)],[(0,100),(6,20)],"فشل الكبد – سوء التغزية","عند وجود أمراض فى الكلى مثل الفشل الكلوى– الجفاف – فشل القلب- نزيف في الجهاز الهضمى"))
startTest.append(Test(["Diabetes"],"Insulin","digit",[(0,100),(2,25)],[(0,100),(2,25)],"نقص نسبة الأنسولين فى الدم و ان كانت نسبة الجلوكوز فى الدم مرتفعه ،، فهذا يسبب مرض السكر ","زيادة نسبة الأنسولين تعنى أرتفاع نسبى الجلوكوز - السكر - فى الدم"))
startTest.append(Test(["Liver Diseases"],"Bilirubin, Total","digit",[(0,100),(1.9,1.9)],[(0,100),(1.9,1.9)],"لا يقل","يزيد بسبب الصفرا و أمراض الكبد ويسبب اصفرار لون العين و ذلك عند اختلال وظائف الكبد"))
startTest.append(Test(["Lipid Profile"],"Cholesterol","digit",[(0,100),(200,239)],[(0,100),(200,239)],"يقل فى حالة عدم القدرة على امتصاص الدهون ","زيادة نسبة الدهون الثلاثية فى الجسم ويسبب ارتفاعها لأمراض مثل : السكر - أمراض القلب - امراض الكلى"))
startTest.append(Test(["Vitamin"],"Vitamin E","digit",[(0,100),(30,50)],[(0,100),(30,50)],"يقل فى حالة أمراض الانيميا وفقر الدم - سوء التغذية المزمنة - اضرابات سوء الامتصاص ","زيادة نسبة فيتامين e فى الدم "))
startTest.append(Test(["Drug"],"Alcohol","digit",[(0,100),(10,80)],[(0,100),(10,80)],"نسبة طبيعية فى الدم  ","زيادة نسبة الكحول فى الدم وان تجاوزت 300 فهى درجة مميتة "))

testsList = []



testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"D Dimer","digit",[(0,100),(1,500)],[(0,100),(1,500)],"فى حالة استئصال الغدة البار دراقية - قلة افراز الغدة الباردراقية ","التهاب الكبد A,B,C - فشل الكبد - الأورام - الفيروسات"))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"Fibrinogen","digit",[(0,100),(200,400)],[(0,100),(200,400)]," ","يزيد فى حالة الأمراض الخبيثة و أمراض الكبد "))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"PCV","digit",[(0,100),(40.7,50.3)],[(0,100),(36.1,44.3)]," يقل عند الانيميا و فقر الدم","يزيد عند زيادة نسبة الحديد فى الدم"))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","Hematocrit","complete blood picture"],"Haemoglobin","digit",[(0,100),(13.5,17.5)],[(0,100),(12,15.5)],"نزيف – جفاف - فى حالة استئصال الغدة البار دراقية - قلة افراز الغدة الباردراقية - الانيميا - النزيف ","التهاب الكبد A,B,C - فشل الكبد - الأورام - الفيروسات"))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC"],"Iron","digit",[(0,100),(65,175)],[(0,100),(50,170)],"يقل فى حالة الانيميا و حالات فقر الدم ","التهاب الكبد A,B,C - فشل الكبد - الأورام - الفيروسات"))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"Red Blood Count","digit",[(0,100),(4.2,5.4)],[(0,100),(4.2,5.4)],"نزيف - انيميا - فى حالة استئصال الغدة البار دراقية - قلة افراز الغدة الباردراقية ","التهاب الكبد A,B,C - فشل الكبد - الأورام - الفيروسات"))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"MCH","digit",[(0,100),(27,31)],[(0,100),(27,31)],"نزيف - انيميا - فى حالة استئصال الغدة البار دراقية - قلة افراز الغدة الباردراقية ","التهاب الكبد A,B,C - فشل الكبد - الأورام - الفيروسات"))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"MCHC","digit",[(0,100),(32,36)],[(0,100),(32,36)],"نزيف - انيميا - فى حالة استئصال الغدة البار دراقية - قلة افراز الغدة الباردراقية ","التهاب الكبد A,B,C - فشل الكبد - الأورام - الفيروسات"))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"MCV","digit",[(0,100),(78,99)],[(0,100),(78,99)],"نزيف - انيميا - فى حالة استئصال الغدة البار دراقية - قلة افراز الغدة الباردراقية ","التهاب الكبد A,B,C - فشل الكبد - الأورام - الفيروسات"))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"Platelet Count","digit",[(0,100),(140000,440000)],[(0,100),(140000,440000)],"نزيف - انيميا - فى حالة استئصال الغدة البار دراقية - قلة افراز الغدة الباردراقية ","في درجات الحراره المنخفضه – التمرينات العنيفه -التهاب الكبد A,B,C - فشل الكبد - الأورام - الفيروسات"))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"WBCs Count","digit",[(0,100),(4000,11000)],[(0,100),(4000,11000)],"نزيف - انيميا - فى حالة استئصال الغدة البار دراقية - قلة افراز الغدة الباردراقية ","التهاب الكبد A,B,C - فشل الكبد - الأورام - الفيروسات - زيادة افراز الغدة الدرقيه - الحروق و الجروح "))


testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"Haematocrit","digit",[(0,100),(37,47)],[(0,100),(37,47)],"",""))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"RDW","digit",[(0,100),(11.6,14)],[(0,100),(11.6,14)],"",""))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"Leucocytic Count","digit",[(0,100),(4000,10500)],[(0,100),(4000,10500)],"",""))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"Basophils","digit",[(0,100),(0,199)],[(0,100),(0,199)],"زيادة افراز الغدة الدرقية - اثناء فترة التبويض - الحمل - الضغط النفسى","فى بعض حالات الانيميا"))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"Eosinophils","digit",[(0,100),(0,499)],[(0,100),(0,499)],"فى حالات الحروق - ","الحساسية مثل أزمة الربو - درجة حرارى الجسم المرتفة - أمراض جلدية مثل(كريما-الصدفية-التهاب الجلد) - سرطان الدم-التمارين العنيفة"))
#testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"Staff","digit",[(0,100),(37,47)],[(0,100),(37,47)],"",""))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"Segmented","digit",[(0,100),(2000,6500)],[(0,100),(2000,6500)],"",""))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"Lymphocytes","digit",[(0,100),(1500,3500)],[(0,100),(1500,3500)],"داء الضرن - فشل القلب - الفشل الكلوى","زيادة الأمراض المناعية - نقص هرمون الأندرينالين -زيادة افرازات الغدة الدرقية "))
testsList.append(Test(["Blood Diseases"," Complete Blood Count","CBC","complete blood picture"],"Monocytes","digit",[(0,100),(300,1000)],[(0,100),(300,1000)],"","أى التهاب أو عدوى بكتيريه - مرض الذئبة الحمراء - سرطان الدم"))





testsList.append(Test(["Clinical chemistry"],"Urea","digit",[(0,100),(6,20)],[(0,100),(6,20)],"لا يقل","عند وجود أمراض فى الكلى مثل الفشل الكلوى"))
testsList.append(Test(["Clinical chemistry"],"Uric Acid","digit",[(0,100),(4.5,8)],[(0,100),(2.5,6.2)],"لا يقل","يزيد عند مرض النقرص"))
testsList.append(Test(["Clinical chemistry"],"Creatinine","digit",[(0,100),(.7,1.3)],[(0,100),(.6,1.1)],"لا يقل","عند وجود أمراض فى الكلى مثل الفشل الكلوى - داء العملقة – اكروميجالي(ضخامة الاطراف)"))
testsList.append(Test(["Clinical chemistry"],"GGT","digit",[(0,100),(5,85)],[(0,100),(5,85)],"لا يقل","انسداد القنوات المرارية"))
testsList.append(Test(["Clinical chemistry"],"CA","digit",[(0,100),(8.5,10.1)],[(0,100),(8.5,10.1)],"فى حالة استئصال الغدة البار دراقية - قلة افراز الغدة الباردراقية ","التهاب الكبد A,B,C - فشل الكبد - الأورام - الفيروسات"))



testsList.append(Test(["Diabetes"],"Insulin","digit",[(0,100),(2,25)],[(0,100),(2,25)],"نقص نسبة الأنسولين فى الدم و ان كانت نسبة الجلوكوز فى الدم مرتفعه- فهذا يسبب مرض السكر ","زيادة نسبة الأنسولين تعنى أرتفاع نسبى الجلوكوز - السكر - فى الدم"))
testsList.append(Test(["Diabetes"],"Glucose Blood","digit",[(0,100),(65,95)],[(0,100),(65,95)],"فى حالة نقص نسبة الجلوكوز - السكر فى الدم ","أرتفاع نسبة الجلوكوز - السكر - فى الدم "))
testsList.append(Test(["Diabetes"],"CA","digit",[(0,100),(8.5,10.1)],[(0,100),(8.5,10.1)],"فى حالة استئصال الغدة البار دراقية - قلة افراز الغدة الباردراقية ","التهاب الكبد A,B,C - فشل الكبد - الأورام - الفيروسات"))



testsList.append(Test(["Liver Diseases"],"ALbumin","digit",[(0,100),(3.4,5)],[(0,100),(3.4,5)],"يقل فى حالات سوء التغذية - يقل فى حالة أمراض الكبد","لا يزيد"))
testsList.append(Test(["Liver Diseases"],"Aspartate Aminotransferase","digit",[(0,100),(37,100)],[(0,100),(37,100)],"لا يقل","التهاب الكبد A,B,C - فشل الكبد - الأورام - الفيروسات - التمارين العنيفه- اصابة او مرض العضلات الهيكلية-التمارين العنيفة"))
testsList.append(Test(["Liver Diseases"],"Bil D","digit",[(0,100),(.3,100)],[(0,100),(.3,100)],"لا يقل","يزيد بسبب الصفرا و أمراض الكبد ويسبب اصفرار لون العين"))
testsList.append(Test(["Liver Diseases"],"Bilirubin, Direct","digit",[(0,100),(.3,100)],[(0,100),(.3,100)],"لا يقل","يزيد بسبب الصفرا و أمراض الكبد ويسبب اصفرار لون العين"))
testsList.append(Test(["Liver Diseases"],"Bil T","digit",[(0,100),(1.9,1.9)],[(0,100),(1.9,1.9)],"لا يقل","يزيد بسبب الصفرا و أمراض الكبد ويسبب اصفرار لون العين"))
testsList.append(Test(["Liver Diseases"],"Bilirubin, Total","digit",[(0,100),(1.9,1.9)],[(0,100),(1.9,1.9)],"لا يقل","يزيد بسبب الصفرا و أمراض الكبد ويسبب اصفرار لون العين"))


testsList.append(Test(["Lipid Profile"],"Triglycerides","digit",[(0,100),(150,199)],[(0,100),(150,199)],"يقل فى حالة عدم القدرة على امتصاص الدهون ","زيادة نسبة الدهون الثلاثية فى الجسم ويسبب ارتفاعها لأمراض مثل : السكر - أمراض القلب - امراض الكلى"))
testsList.append(Test(["Lipid Profile"],"Cholesterol","digit",[(0,100),(200,239)],[(0,100),(200,239)],"يقل فى حالة عدم القدرة على امتصاص الدهون ","زيادة نسبة الدهون الثلاثية فى الجسم ويسبب ارتفاعها لأمراض مثل : السكر - أمراض القلب - امراض الكلى"))


testsList.append(Test(["Vitamin"],"Vitamin ِِA","digit",[(0,100),(30,80)],[(0,100),(30,80)],"يقل فى حالة أمراض الانيميا وفقر الدم ","زيادة نسبة فيتامين أ فى الدم "))
testsList.append(Test(["Vitamin"],"Vitamin E","digit",[(0,100),(30,50)],[(0,100),(30,50)],"يقل فى حالة أمراض الانيميا وفقر الدم - سوء التغذية المزمنة - اضرابات سوء الامتصاص ","زيادة نسبة فيتامين e فى الدم "))

#testsList.append(Test(["Drug"],"Alcohol","digit",[(0,100),(10,80)],[(0,100),(10,80)],"نسبة طبيعية فى الدم  ","زيادة نسبة الكحول فى الدم وان تجاوزت 300 فهى درجة مميتة "))





for test in startTest:
    for cat in test.category:
     pickle.dump(test, open(cat.lower()+".bin", "wb"))

for test in testsList:
    for cat in test.category:
      pickle.dump(test, open(cat.lower()+".bin", "ab"))



def match(lineList):
    print(lineList)
    finalTests=[]
    tests = []
    lineListTypes=[]
    result=[]
    fileFlag=False #check if the file name was read fron image
    startCounter=0
    filesList=("Liver Diseases","Blood Diseases","Complete Blood Count","CBC","Clinical chemistry","complete blood picture","Vitamin","Drug","Lipid Profile")
    s= lineList[0] # file name in the first line
    s=s[:-1]
    fileFromList = s.lower().split(" ")
    for file in filesList:
        fileNamesplits = file.lower().split(" ")

        if len(fileFromList)==len(fileNamesplits):
         i=0
         for fn in fileNamesplits:
            ratio = difflib.SequenceMatcher(None, fn, fileFromList[i]).ratio()
            if ratio >= 0.5:
                i += 1

                if i==len(fileFromList):
                    lineList[0]=file
                    fileFlag=True
                    startCounter=1


            else:
             break


    if fileFlag==True:
        with (open(lineList[0] + ".bin", "rb")) as openfile:  # file name will be determined by category name from the test
            while True:
                try:
                    tests.append(pickle.load(openfile))

                except EOFError:
                    break
    else:
        for file in filesList:
            with (open(file + ".bin","rb")) as openfile:  # file name will be determined by category name from the test
                while True:
                    try:
                        tests.append(pickle.load(openfile))

                    except EOFError:
                        break

    for i in range(startCounter, len(lineList)):
        flag=False
        maxRatio=0.0
        tempTestName=Test([],"not matched","none",[],[],"","")

        for test in tests:

            ratio = difflib.SequenceMatcher(None, test.name, lineList[i]).ratio()
            if ratio >= 0.5 and len(test.name)>1:
                flag=True
               # print("matched with : " + test.name)
                if maxRatio<ratio:
                    tempTestName=test

                    maxRatio=ratio
        #            print(ratio)


        lineList[i] = tempTestName.name
       # print("matched with : " + tempTestName.name)
        lineListTypes.append(tempTestName.type)
        finalTests.append(tempTestName)

    lineListTypes.append(finalTests)
    return lineListTypes

#types=match(["CDMPLETE BLDDD PfCTCRE ",""])
#print(types)




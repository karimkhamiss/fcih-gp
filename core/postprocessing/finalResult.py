import pickle

from core.postprocessing.postproccessing import Test
def getTestResult(tests,age,gender):
    resultsDes=[]

    if gender == "male":
        for j in range(0,len(tests[1])):
          i = 0
          testObj = tests[1][j]
          if testObj.name=="not matched":

              continue
          result = float(tests[2][j].replace(" ",'').replace("%",''))
          leng=len(testObj.male)-1

          while i<leng:
              if testObj.male[i][0]<= age and testObj.male[i][1] >=age:
                  if testObj.male[i+1][0]<= result and testObj.male[i+1][1] >=result:
                      resultsDes.append("Normal Range")
                  elif result>testObj.male[i+1][1]:
                      resultsDes.append("High Range in case : " + testObj.increase)
                  elif result<testObj.male[i+1][0]:
                      resultsDes.append("Low Range in case : " + testObj.decrease)
              else:
                  i=i+2
    else:
        for j in range(0,len(tests[1])):
            testObj=tests[1][j]
            i = 0
            if testObj.name == "not matched":
                continue
            result = float(tests[2][j].replace(" ",'').replace("%",''))
            while i <len(testObj.female)-1:
                if testObj.female[i][0] <= age and testObj.female[i][1] >= age:
                    if testObj.female[i + 1][0] <= result and testObj.female[i + 1][1] >= result:
                        resultsDes.append("Normal Range")
                    elif result > testObj.female[i + 1][1]:
                        resultsDes.append("High Range in case : " + testObj.increase)
                    elif result < testObj.female[i + 1][0]:
                        resultsDes.append("Low Range in case : " + testObj.decrease)
                else:
                    i = i + 2

    return resultsDes
# test=Test(["Liver Diseases"],"ALbumin","digit",[(0,10),(3.4,5),(11,100),(7,10)],[(0,100),(3.4,5)],"يقل فى حالات سوء التغذية - يقل فى حالة أمراض الكبد"," يزيد عند وجود أمراض فى الكلى مثل الفشل الكلوى")
# print(getTestResult(test,11,11,"male"))

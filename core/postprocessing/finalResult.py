from core.postprocessing.postproccessing import Test
def getTestResult(test,age,result,gender):
    if gender=="male":
      for i in range(0,len(test.male)):
          if test.male[i][0]<= age and test.male[i][1] >=age:
              if test.male[i+1][0]<= result and test.male[i+1][1] >=result:
                  return "Normal Range"
              elif result>test.male[i+1][1]:
                  return "High Range in case :\n " + test.increase
              elif result<test.male[i+1][0]:
                  return "Low Range in case :\n " + test.decrease
          else:
              i=i+2
    else:
        for i in range(0, len(test.female)):
            if test.female[i][0] <= age and test.female[i][1] >= age:
                if test.female[i + 1][0] <= result and test.female[i + 1][1] >= result:
                    return "Normal Range"
                elif result > test.female[i + 1][1]:
                    return "High Range in case :\n " + test.increase
                elif result < test.female[i + 1][0]:
                    return "Low Range in case :\n " + test.decrease
            else:
                i = i + 2


test=Test(["Liver Diseases"],"ALbumin","digit",[(0,10),(3.4,5),(11,100),(7,10)],[(0,100),(3.4,5)],"يقل فى حالات سوء التغذية - يقل فى حالة أمراض الكبد"," يزيد عند وجود أمراض فى الكلى مثل الفشل الكلوى")
print(getTestResult(test,11,11,"male"))

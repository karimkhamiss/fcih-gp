class User:
    id = ""
    first_name =""
    last_name = ""
    gender = ""
    age = ""
    medical_histories = []
    def __init__(self,id,first_name,last_name,gender_id,age):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        if gender_id == 1:
            self.gender = "male"
        else:
            self.gender = "female"
        self.age = age


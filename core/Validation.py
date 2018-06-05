import re


class validation():
    def check_empty(sr):
        if sr == '':
            return True
            print("Erorr")
        else:
            return False
            print("Done")


    def check_date(input_date):
        match=re.match(r'(\d+/\d+/\d{4})',input_date)
        if match== None:
            print("Error")
            return False
        else:
            print("Done")
            return True

    def check_name(input_str):
        match=re.match(r'(^[a-zA-Z]+)|(^[a-zA-Z]+[0-9])',input_str)
        if match== None:
            print("Error")
            return False
        else:
            print("Done")
            return True
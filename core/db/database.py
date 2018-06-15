#!/usr/bin/python

import sqlite3
from random import randint
from core.data_structure.User import User
# conn = sqlite3.connect('db.db')
# c=conn.cursor()
import datetime

# categories = [
#     "Liver Diseases",
#     "Clinical chemistry",
#     "Diabetes",
#     "Lipid Profile",
#     "Vitamin",
#     "Drug",
#     "complete blood picture"
# ]
# category_1_tests = [
#     "Bilirubin, Total",
#     "ALbumin",
#     "Aspartate Aminotransferase",
#     "Bil D",
#     "Bilirubin, Direct",
#     "Bil T",
# ]
# category_2_tests = [
#     "Urea",
#     "Uric Acid",
#     "Creatinine",
#     "GGT",
#     "CA",
# ]
# category_3_tests = [
#     "Insulin",
#     "Glucose Blood",
#     "CA",
# ]
# category_4_tests = [
#     "Lipid Profile",
#     "Cholesterol",
#     "Triglycerides",
# ]
# category_5_tests = [
#     "Vitamin E",
#     "Vitamin A",
# ]
# category_6_tests = [
#     "Alcohol"
# ]
# category_7_tests = [
#     "D Dimer",
#     "Fibrinogen",
#     "PCV",
#     "Haemoglobin",
#     "Iron",
#     "Red Blood Count",
#     "MCH",
#     "MCHC",
#     "MCV",
#     "Platelet Count",
#     "WBCs Count",
# ]c
def create_tabels():

    c.execute('''CREATE TABLE IF NOT EXISTS genders (
     id integer NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
     type text NOT NULL
    );''')

    c.execute('''CREATE TABLE IF NOT EXISTS users (
     id integer NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
     first_name text NOT NULL,
     last_name text NOT NULL,
     gender_id integer Not NULL,
     birthdate text NOT NULL,
     username text NOT NULL,
     password text NOT NULL,
     FOREIGN KEY (gender_id) REFERENCES genders(id)
    );''')

    c.execute('''CREATE TABLE IF NOT EXISTS categories(
     id integer NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
     name text NOT NULL
    );''')

    c.execute('''CREATE TABLE IF NOT EXISTS tests(
     id integer NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
     name text NOT NULL,
     category_id integer NOT NULL,
     FOREIGN KEY (category_id) REFERENCES categories(id)
    );''')

    c.execute('''CREATE TABLE IF NOT EXISTS medical_histories (
     id integer NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
     category_name integer NOT NULL,
     user_id integer NOT NULL,
     date text NOT NULL,
     FOREIGN KEY (user_id) REFERENCES users(id)
    );''')
    c.execute('''CREATE TABLE IF NOT EXISTS medical_histories_tests (
     id integer NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
     medical_history_id integer NOT NULL,
     test_id integer NOT NULL,
     value text NOT NULL,
     description text,
    FOREIGN KEY (medical_history_id) REFERENCES medical_histories(id),
    FOREIGN KEY (test_id) REFERENCES tests(id)
    );''')
    print("Tables created successfully")
def data_entry():
    c.execute('''INSERT INTO genders ('type') VALUES('male');''')
    c.execute('''INSERT INTO genders ('type') VALUES('female');''')

    # c.execute('''INSERT INTO users ('first_name','last_name','gender','age') VALUES ('Karim','Khamiss',1,'21');''')
    for category in categories :
        query = "insert into categories ('name') VALUES ('" + category + "')"
        c.execute(query)
    for test in category_1_tests :
        query = "insert into tests ('name','category_id') VALUES ('" + test + "',1)"
        c.execute(query)
    for test in category_2_tests :
        query = "insert into tests ('name','category_id') VALUES ('" + test + "',2)"
        c.execute(query)
    for test in category_3_tests :
        query = "insert into tests ('name','category_id') VALUES ('" + test + "',3)"
        c.execute(query)
    for test in category_4_tests :
        query = "insert into tests ('name','category_id') VALUES ('" + test + "',4)"
        c.execute(query)
    for test in category_5_tests :
        query = "insert into tests ('name','category_id') VALUES ('" + test + "',5)"
        c.execute(query)
    for test in category_6_tests :
        query = "insert into tests ('name','category_id') VALUES ('" + test + "',6)"
        c.execute(query)
    for test in category_7_tests :
        query = "insert into tests ('name','category_id') VALUES ('" + test + "',7)"
        c.execute(query)
    print("Data entry Done")
def open_db():
    connection = sqlite3.connect('..\db\db.db')
    return connection
def commit(connection):
    connection.commit()
def close(connection):
    connection.close()
current_user = User(0,"","","","")
def check_unique(username):
    connection = open_db()
    c = connection.cursor()
    query = "SELECT * FROM users where username = '"+username+"'"
    c.execute(query)
    data = c.fetchall()
    close(connection)
    if(len(data)>0):
        return 1
    else:
        return 0
def login(username,password):
    connection = open_db()
    c = connection.cursor()
    query = "SELECT * FROM users where username = '"+username+"' and password = '"+password+"'"
    c.execute(query)
    data = c.fetchall()
    close(connection)
    if(len(data)>0):
        global current_user
        current_user = User(data[0][0],data[0][1],data[0][2],data[0][3],get_age(data[0][4]))
        set_medical_histories()
    return data
def get_current_user():
    global current_user
    return current_user
def signup(first_name,last_name,birthdate,gender,username,password):
    connection = open_db()
    c = connection.cursor()
    query = "insert into users ('first_name','last_name','gender_id','birthdate','username','password') " \
            "VALUES ('" + first_name + "' ,'" + last_name + "','" + str(gender) + "','" + str(birthdate) + "','" + username + "' ,'" + password + "')"
    c.execute(query)
    commit(connection)
    close(connection)
    login(username,password)
def get_user_id():
    global current_user
    return current_user.id
def get_age(birthdate):
    birthdate = birthdate.split("/")
    day = int(birthdate[0])
    month = int(birthdate[1])
    year = int(birthdate[2])
    today = datetime.date.today()
    return today.year - year - ((today.month, today.day) < (month, day))
def get_test_name(test_id):
    connection = open_db()
    c = connection.cursor()
    query = "SELECT name FROM tests WHERE id = "+ str(test_id)+""
    c.execute(query)
    data = c.fetchall()
    close(connection)
    return data[0][0]
def get_user_name():
    connection = open_db()
    c = connection.cursor()
    query = "SELECT first_name,last_name FROM users WHERE id = "+ str(get_user_id())+""
    c.execute(query)
    data = c.fetchall()
    close(connection)
    return data[0][0]+" "+data[0][1]
def get_test_id(test_name):
    connection = open_db()
    c = connection.cursor()
    query = "SELECT * FROM tests where name = '"+test_name+"'"
    c.execute(query)
    data = c.fetchall()
    close(connection)
    return data[0][0]
def add_medical_history(category_name):
    connection = open_db()
    c = connection.cursor()
    date = datetime.datetime.today().strftime('%d/%m/%Y')
    query = "insert into medical_histories ('category_name','user_id','date') " \
        "VALUES ('" + category_name + "','" + str(get_user_id()) + "','" + date + "')"
    c.execute(query)
    commit(connection)
    close(connection)
def add_medical_history_test(test):
    connection = open_db()
    c = connection.cursor()
    medical_history_id = get_medical_history_id()
    # print(test[0])
    test_id = get_test_id(test[0])
    query = "insert into medical_histories_tests ('medical_history_id','test_id','value','description') " \
            "VALUES ('" + str(medical_history_id) + "' ,'" + str(test_id) + "','" + str(test[1]) + "','" + test[2] + "')"
    c.execute(query)
    commit(connection)
    close(connection)
def get_medical_history_id():
    connection = open_db()
    c = connection.cursor()
    query = "SELECT id FROM medical_histories ORDER BY id DESC LIMIT 1"
    c.execute(query)
    data = c.fetchall()
    close(connection)
    return data[0][0]
def save_test(category_name,tests):
    add_medical_history(category_name)
    for test in tests:
        add_medical_history_test(test)
    pass
def get_medical_history_category(id):
    connection = open_db()
    c = connection.cursor()
    query = "SELECT category_name FROM medical_histories WHERE id = " + str(id) + ""
    c.execute(query)
    data = c.fetchall()
    close(connection)
    return data[0][0]
def set_medical_histories():
    print("User id =",get_user_id())
    connection = open_db()
    c = connection.cursor()
    query = "SELECT id,category_name,date FROM medical_histories WHERE user_id = "+ str(get_user_id())+""
    c.execute(query)
    data = c.fetchall()
    close(connection)
    global current_user
    current_user.medical_histories = data
def get_medical_history_test(medical_history_id):
    connection = open_db()
    c = connection.cursor()
    query = "SELECT test_id,value,description FROM medical_histories_tests WHERE medical_history_id = " + str(medical_history_id) + ""
    c.execute(query)
    data = c.fetchall()
    close(connection)
    return data
def logout():
    global current_user
    print("Before Logout" + current_user.first_name)
    current_user = User("", "", "", "", "")
    current_user.medical_histories = []
    print("After Logout" + current_user.first_name)
# login("karim","123")
# print("After Login " , current_user.medical_histories)
# logout()
# print("After Logout " , current_user.medical_histories)
# set_medical_histo/ries()
# print(current_user.medical_histories)
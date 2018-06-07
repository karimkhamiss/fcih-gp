#!/usr/bin/python

import sqlite3
from random import randint

conn = sqlite3.connect('db.db')
c=conn.cursor()
from datetime import date
categories = [
    "Liver Diseases",
    "Clinical chemistry",
    "Diabetes",
    "Lipid Profile",
    "Vitamin",
    "Drug",
    "complete blood picture"
]
category_1_tests = [
    "Bilirubin, Total",
    "ALbumin",
    "Aspartate Aminotransferase",
    "Bil D",
    "Bilirubin, Direct",
    "Bil T",
]
category_2_tests = [
    "Urea",
    "Uric Acid",
    "Creatinine",
    "GGT",
    "CA",
]
category_3_tests = [
    "Insulin",
    "Glucose Blood",
    "CA",
]
category_4_tests = [
    "Lipid Profile",
    "Cholesterol",
    "Triglycerides",
]
category_5_tests = [
    "Vitamin E",
    "Vitamin A",
]
category_6_tests = [
    "Alcohol"
]
category_7_tests = [
    "D Dimer",
    "Fibrinogen",
    "PCV",
    "Haemoglobin",
    "Iron",
    "Red Blood Count",
    "MCH",
    "MCHC",
    "MCV",
    "Platelet Count",
    "WBCs Count",
]
print(categories)
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
    print("Opened database successfully")
    return connection
def commit(connection):
    connection.commit()
def close(connection):
    connection.close()

def login(username,password):
    connection = open_db()
    c = connection.cursor()
    query = "SELECT * FROM users where username = '"+username+"' and password = '"+password+"'"
    c.execute(query)
    data = c.fetchall()
    close(connection)
    return data
def signup(first_name,last_name,birthdate,gender,username,password):
    connection = open_db()
    c = connection.cursor()
    query = "insert into users ('first_name','last_name','gender_id','birthdate','username','password') " \
            "VALUES ('" + first_name + "' ,'" + last_name + "','" + str(gender) + "','" + str(birthdate) + "','" + username + "' ,'" + password + "')"
    c.execute(query)
    commit(connection)
    close(connection)
def add_user():
    pass
def get_users():
    pass
def get_user_id():
    connection = open_db()
    c = connection.cursor()
    query = "SELECT id FROM users ORDER BY id DESC LIMIT 1"
    c.execute(query)
    data = c.fetchall()
    close(connection)
    return data[0][0]
def get_age():
    birthdate = get_birthdate()
    birthdate = birthdate.split("/")
    day = int(birthdate[0])
    month = int(birthdate[1])
    year = int(birthdate[2])
    today = date.today()
    return today.year - year - ((today.month, today.day) < (month, day))

def get_birthdate():
    connection = open_db()
    c = connection.cursor()
    query = "SELECT birthdate FROM users WHERE id = "+ str(get_user_id())+""
    c.execute(query)
    data = c.fetchall()
    close(connection)
    return data[0][0]
def get_gender_type():
    connection = open_db()
    c = connection.cursor()
    query = "SELECT type FROM genders JOIN users ON users.gender_id = genders.id WHERE users.id = "+ str(get_user_id())+""
    c.execute(query)
    data = c.fetchall()
    close(connection)
    return data[0][0]
def get_test_id(test_name):
    connection = open_db()
    c = connection.cursor()
    query = "SELECT id FROM tests WHERE name = "+test_name+""
    c.execute(query)
    data = c.fetchall()
    close(connection)
    return data[0][0]
def add_medical_history(category_name):
    connection = open_db()
    c = connection.cursor()
    query = "insert into medical_histories ('category_name','user_id','date') " \
            "VALUES ('" + category_name + "' ,'" + last_name + "','" + str(get_user_id()) + "','" + date + "')"
    c.execute(query)
    commit(connection)
    close(connection)

def save_test(test_id,test_value,description,user_id):
    pass

create_tabels() # Function To Creat Tabels
data_entry() #Function To Fill Tabels (Enter Data To Tabels)
commit(conn)
close(conn)
# login("karim","123") #Function To Read and Retrive data from tabels
# first_name = "Karim"
# last_name = "Khamiss"
# age = 222
# gender = 2
# signup(first_name,last_name,age,gender,"karim","12aa3")
# query = "insert into users ('first_name','last_name','gender','age') VALUES ('"+first_name+"' ,'"+last_name+"',1,22)"
# print(query)
#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('App_DB.db')
c=conn.cursor()
print ("Opened database successfully")

def create_tabels():

    c.execute('''CREATE TABLE IF NOT EXISTS Gender (
     gender_id integer NOT NULL UNIQUE PRIMARY KEY,
     type text NOT NULL
    );''')

    c.execute('''CREATE TABLE User (
     user_id integer NOT NULL UNIQUE PRIMARY KEY,
     first_name text NOT NULL,
     last_name text NOT NULL,
     gender_id integer Not NULL,
     birthday text NOT NULL,
     email text NOT NULL,
     password text NOT NULL,
     FOREIGN KEY (gender_id) REFERENCES Gender(gender_id)
    );''')

    c.execute('''CREATE TABLE Test_Categories(
     category_id integer NOT NULL UNIQUE PRIMARY KEY,
     name text NOT NULL
    );''')

    c.execute('''CREATE TABLE Tests(
     test_id integer NOT NULL UNIQUE PRIMARY KEY,
     name text NOT NULL,
     category_id integer NOT NULL,
     FOREIGN KEY (category_id) REFERENCES Test_Categories(category_id)
    );''')

    c.execute('''CREATE TABLE Medical_History (
     medical_id integer NOT NULL UNIQUE PRIMARY KEY,
     test_id integer NOT NULL,
     percetage text NOT NULL,
     description text NOT NULL,
     user_id integer NOT NULL,
     date text NOT NULL,
     FOREIGN KEY (test_id) REFERENCES Tests(test_id),
     FOREIGN KEY (user_id) REFERENCES User(user_id)
    );''')



    print("Tables created successfully")

def data_entry():
    c.execute('''INSERT INTO Gender VALUES(1,'male');''')
    c.execute('''INSERT INTO Gender VALUES(2,'female');''')

    c.execute('''INSERT INTO User VALUES(1,'Mohamed','Osama',1,'10/10/2018','mohamed@yahoo.com','m1m1');''')
    c.execute('''INSERT INTO User VALUES(2,'karim','khamiss',1,'20/20/2018','karim@yahoo.com','k1k1');''')
    c.execute('''INSERT INTO User VALUES(3,'aya','mohamed',2,'30/30/2018','aya@yahoo.com','aya1aya1');''')

    c.execute('''INSERT INTO Test_Categories VALUES(1,'category1');''')
    c.execute('''INSERT INTO Test_Categories VALUES(2,'category2');''')
    c.execute('''INSERT INTO Test_Categories VALUES(3,'category3');''')

    c.execute('''INSERT INTO Tests VALUES(1,'test1',3);''')
    c.execute('''INSERT INTO Tests VALUES(2,'test2',2);''')
    c.execute('''INSERT INTO Tests VALUES(3,'test3',1);''')

    c.execute('''INSERT INTO Medical_History VALUES(1,3,'70%','medical1',1,'01/01/2018');''')
    c.execute('''INSERT INTO Medical_History VALUES(2,2,'50%','medical1',2,'02/02/2018');''')
    c.execute('''INSERT INTO Medical_History VALUES(3,1,'20%','medical1',3,'03/03/2018');''')





    print("Data entry Done")

def Read_Data():
    c.execute('''
    SELECT * 
    FROM User
    JOIN Medical_History ON Medical_History.user_id = User.user_id
    JOIN Tests ON Tests.test_id = Medical_History.test_id
    JOIN Test_Categories ON Test_Categories.category_id = Tests.category_id
    WHERE Test_Categories.name = 'category2'
    ''')
    data = c.fetchall()
    print("Select 1 : ")
    print(data)

    c.execute('''
    select User.first_name , User.last_name 
    from User join Medical_History 
    where User.user_id = Medical_History.user_id and Medical_History.percetage='20%'
    ''')

    data = c.fetchall()
    print("Select 2 : ")
    print(data)

    c.execute('''
    select * from User
    ''')

    data = c.fetchall()
    print("Select 3 : ")
    print(data)

    c.execute('''
    select * from User join Gender where Gender.gender_id = User.gender_id and Gender.type='male'
    ''')

    data = c.fetchall()
    print("Select 4 : ")
    print(data)
    print("Read Done ")



create_tabels() # Function To Creat Tabels
data_entry() #Function To Fill Tabels (Enter Data To Tabels)
Read_Data() #Function To Read and Retrive data from tabels

conn.commit()
conn.close()
conn.close()
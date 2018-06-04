#!/usr/bin/python

import sqlite3

# conn = sqlite3.connect('db.db')
# c=conn.cursor()

# def create_tabels():
#
#     c.execute('''CREATE TABLE IF NOT EXISTS genders (
#      id integer NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
#      type text NOT NULL
#     );''')
#
#     c.execute('''CREATE TABLE IF NOT EXISTS users (
#      id integer NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
#      first_name text NOT NULL,
#      last_name text NOT NULL,
#      gender_id integer Not NULL,
#      age integer NOT NULL,
#      FOREIGN KEY (gender_id) REFERENCES genders(id)
#     );''')
#     c.execute('''CREATE TABLE IF NOT EXISTS main_users (
#      id integer NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
#       user_id integer NOT NULL,
#      email text NOT NULL,
#      password text NOT NULL,
#      FOREIGN KEY (user_id) REFERENCES users(id)
#     );''')
#     c.execute('''CREATE TABLE IF NOT EXISTS user_users (
#      id integer NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
#      user_id integer NOT NULL,
#      main_user_id integer NOT NULL,
#      FOREIGN KEY (user_id) REFERENCES users(id)
#      FOREIGN KEY (main_user_id) REFERENCES main_users(id)
#     );''')
#     c.execute('''CREATE TABLE IF NOT EXISTS user_users (
#      id integer NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
#      first_name text NOT NULL,
#      last_name text NOT NULL,
#      gender_id integer Not NULL,
#      age integer NOT NULL,
#      main_user_id text NOT NULL,
#      FOREIGN KEY (main_user_id) REFERENCES main_users(id)
#      FOREIGN KEY (gender_id) REFERENCES genders(id)
#     );''')
#
#     c.execute('''CREATE TABLE IF NOT EXISTS categories(
#      id integer NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
#      name text NOT NULL
#     );''')
#
#     c.execute('''CREATE TABLE IF NOT EXISTS tests(
#      id integer NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
#      name text NOT NULL,
#      category_id integer NOT NULL,
#      FOREIGN KEY (category_id) REFERENCES categories(id)
#     );''')
#
#     c.execute('''CREATE TABLE IF NOT EXISTS medical_histories (
#      id integer NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
#      test_id integer NOT NULL,
#      percetage text NOT NULL,
#      description text NOT NULL,
#      user_id integer NOT NULL,
#      date text NOT NULL,
#      FOREIGN KEY (test_id) REFERENCES tests(id),
#      FOREIGN KEY (user_id) REFERENCES users(id)
#     );''')
#     print("Tables created successfully")

# def data_entry():
#     c.execute('''INSERT INTO genders ('type') VALUES('male');''')
#     c.execute('''INSERT INTO genders ('type') VALUES('female');''')
#
#     # c.execute('''INSERT INTO users ('first_name','last_name','gender','age') VALUES ('Karim','Khamiss',1,'21');''')
#     # c.execute('''INSERT INTO main_users VALUES(1,'karim','123');''')
#     # c.execute('''INSERT INTO user_users VALUES(1,1);''')
#
#     # c.execute('''INSERT INTO categories VALUES(1,'category1');''')
#     # c.execute('''INSERT INTO categories VALUES(2,'category2');''')
#     # c.execute('''INSERT INTO categories VALUES(3,'category3');''')
#     #
#     # c.execute('''INSERT INTO tests VALUES(1,'test1',3);''')
#     # c.execute('''INSERT INTO tests VALUES(2,'test2',2);''')
#     # c.execute('''INSERT INTO tests VALUES(3,'test3',1);''')
#     #
#     # c.execute('''INSERT INTO medical_histories VALUES(1,3,'70%','medical1',1,'01/01/2018');''')
#     # c.execute('''INSERT INTO medical_histories VALUES(2,2,'50%','medical1',2,'02/02/2018');''')
#     # c.execute('''INSERT INTO medical_histories VALUES(3,1,'20%','medical1',3,'03/03/2018');''')
#
#
#
#
#
#     print("Data entry Done")
def open_db():
    connection = sqlite3.connect('db.db')
    print("Opened database successfully")
    return connection
def commit(connection):
    connection.commit()
def close(connection):
    connection.close()

def login(email,password):
    connection = open_db()
    c = connection.cursor()
    query = "SELECT * FROM main_users where email = '"+email+"' and password = '"+password+"'"
    c.execute(query)
    data = c.fetchall()
    return data
    close(connection)
def signup(first_name,last_name,age,gender,email,password):
    connection = open_db()
    c = connection.cursor()
    query = "insert into users ('first_name','last_name','gender_id','age') VALUES ('" + first_name + "' ,'" + last_name + "','" + str(gender) + "','" + str(age) + "')"
    c.execute(query)
    commit(connection)
    query = "SELECT id FROM users ORDER BY id DESC LIMIT 1"
    c.execute(query)
    data = c.fetchall()
    query = "insert into main_users ('user_id','email','password') VALUES ('" + str(data[0][0]) + "','" + email + "' ,'" + password + "')"
    c.execute(query)
    commit(connection)
    close(connection)
def add_user():
    pass
def get_users():
    pass

# create_tabels() # Function To Creat Tabels
# data_entry() #Function To Fill Tabels (Enter Data To Tabels)
# login("karim","123") #Function To Read and Retrive data from tabels
# first_name = "Karim"
# last_name = "Khamiss"
# age = 222
# gender = 2
# signup(first_name,last_name,age,gender,"karim","12aa3")
# query = "insert into users ('first_name','last_name','gender','age') VALUES ('"+first_name+"' ,'"+last_name+"',1,22)"
# print(query)
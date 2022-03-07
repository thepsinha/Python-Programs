import sqlite3
import pandas
class Empl:
    def __init__(self):
        global conn ,c
        conn = sqlite3.connect("Emp.db")
        c = conn.cursor()
        # c.execute("Create table emp (dep_id int primary key,name varchar(20),city varchar(20),department varchar(100),salary varchar(200))")
        # print("Created successfully")
        # conn.commit()
    def insert(self):
        dep_id = int(input("Enter id in Emp Table."))
        name = input("Enter name in Emp Table..")
        city = input("Enter city in Emp Table..")
        department = input("Enter Department in Emp Table..")
        salary = int(input("Enter Salary in Emp Table.."))
        val = [(dep_id,name,city,department,salary),]
        conn.executemany("insert into emp values(?,?,?,?,?)",val)
        print("Inserted.")
        conn.commit()
    def select_data(self):
        result = conn.execute("Select *from emp")
        data = result.fetchall()
        pa = pandas.DataFrame(data,columns=['ID','Name','City','Department','Salary'])
        print(pa)
obj = Empl()
print(obj.insert())
print(obj.select_data())
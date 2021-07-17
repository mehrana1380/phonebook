#import os
import sqlite3
def data_base():
    query= 'insert into phonebook values ("{}", "{}")'
    full_name=""
    while full_name != "exit" :
        full_name=input("enter a name:\n")

        phone=int(input("enter a phone number:\n"))

        cursor.execute(query.format(name, number))

    connection.commit()
    connection.close()

def add(name, number):
    data_base()
    query= 'insert into phonebook values ("{}", "{}")'
    connection= sqlite3.connection("mydb")
    connection.close()

def search(name):
    data_base()
    query_2= 'select * from phonebook'
    for line in query_2.readlines():
        if name== line.split(":")[0]:
            print(name+ ":"+ line.split(":")[1])
    connection= sqlite3.connection("proje.db")
    connection.close()

def delete(name):
    data_base()
    query_2= 'select * from phonebook'
    new_database=""
    for line in query_2.readlines():
        if not name== line.split(":")[0]:
            new_database += line

    connection= sqlite3.connection("proje.db")
    connection.close()

ch= 1
while ch!= 0:
    print("1-add user\n2-search phone\n3-Delete phone\n4-show all numbers\n0-Exit")
    ch=int(input("Enter your choice:\n"))
    #os.system('cls')

    if ch== 1:
        name=input("Enter num")
        number=int(input("Enter num"))
        add(name, number)

    elif ch== 2:
        name=input("Enter num")
        search(name)

    elif ch== 3:
        name=input("Enter num")
        delete(name)

    

#!/usr/bin/python3
''' program to run mysqldb in mysql '''
import sys
import MySQLdb

''' connection to database '''

db = MySQLdb.connect("localhost",sys.argv[1],sys.argv[2],sys.argv[3])
cursor = db.cursor()
cursor.execute("select * from states")

for data in cursor:
    print(data)
''' close the connection '''
db.close()

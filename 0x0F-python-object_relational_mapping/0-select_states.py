#!/usr/bin/python3
''' program to run mysqldb in mysql '''
if __name__ == "__main__":
    import sys
    import MySQLdb

    ''' connection to database '''
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("select * from states")

    for data in cursor:
        print(data)
    ''' close the connection '''
    db.close()

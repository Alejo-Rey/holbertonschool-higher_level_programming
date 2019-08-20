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
    cursor.execute(
            "SELECT cities.name \
                    FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %(id)s", {'id': sys.argv[4]}
            )

    List = []
    for data in cursor.fetchall():
        for x in data:
            List.append(x)
    print(', '.join(List))
    ''' close the connection '''
    db.close()

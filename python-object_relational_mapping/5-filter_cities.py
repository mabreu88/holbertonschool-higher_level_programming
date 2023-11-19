#!/usr/bin/python3
""" a script that takes in an argument and displays all values in the\
    states table of hbtn_0e_0_usa where name matches the argument. """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    c.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id ASC", (argv[4], ))
    lis = c.fetchall()
    if lis is not None:
        print(", ".join([row[1] for row in lis]))
    c.close()
    db.close()

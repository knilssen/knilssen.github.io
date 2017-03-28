'''
Python script that is to familierize myself to the workings about how pyhon interacts
with a Sqlite database, and then ultimatly use this to create a python script to find
and save articles to the database for futher use.

Author: Founding Fathers, Kristian Nilssen
Date: 2/10/2017

Usage:

    python Sqlite_py_practice.py
'''

import sys
import mysql.connector
from mysql.connector import errorcode

def main(url, source, post_date, found_date, title, author, keywords, summary, text):

    config = {
        'user': 'root',
        'password': 'FF_database',
        'host': '127.0.0.1',
        'database': 'ff_database',
        'raise_on_warnings': True,
    }

    try:
        cnx = mysql.connector.connect(**config)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:

        cursor = cnx.cursor()

        add_article = ("INSERT INTO articles "
               "(url, source, post_date, found_date, title, author, keywords, summary, text) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

        data_article = (url, source, post_date, found_date, title, author, keywords, summary, text)

        # Insert new article
        cursor.execute(add_article, data_article)

        # Make sure data is committed to the database
        cnx.commit()

        cursor.close()
        cnx.close()


if __name__ == "__main__":

    if len(sys.argv) != 8:
        print 'usage: python Sqlite_py_practice.py [ url ] [ source ] [ post_date ] [ found_date ] [ title ] [ author ] [ keywords ] [ summary ] [ text ]'
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11], sys.argv[12])

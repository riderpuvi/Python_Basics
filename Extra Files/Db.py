import sys
import mariadb
conn = mariadb.connect(

    user="root",

    password="root",

    host="localhost",

    port = 3306,

    database = "employee",

)

cur= conn.cursor()

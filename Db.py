import sys
import mariadb
conn = mariadb.connect(

    user="root",

    password="puneeth@123",

    host="localhost",

    port = 3306,

    database = "python",

)

cur= conn.cursor()


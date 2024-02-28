# Install mysql on your computer: https://dev.mysql.com/downloads/installer
# pip install mysql 
# pip install mysql-connector or mysql-connector-python

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ehmb2023Initi@ls"
)

# # Prepare a cursor object
cursorObj = db.cursor()

# # Create a database
cursorObj.execute("CREATE DATABASE cwumysqldb1")

print("All done!")


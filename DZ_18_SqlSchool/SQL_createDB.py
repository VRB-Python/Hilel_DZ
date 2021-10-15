import mysql.connector

cnx = mysql.connector.connect(user = "root", password = "1111") # type your username and password
cursor =cnx.cursor()
create_db = f"CREATE DATABASE Bodnar_school;"
cursor.execute(create_db)
cursor.close()
cnx.close()
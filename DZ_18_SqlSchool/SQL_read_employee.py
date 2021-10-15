import mysql.connector

cnx = mysql.connector.connect(user="root", password="1111", database="Bodnar_school")
cursor = cnx.cursor()

query_employee = ("SELECT * from employees")

cursor.execute(query_employee)
all = cursor.fetchall()

for employee in all:
    print(f"Id: {employee[0]}\nName: {employee[1]} {employee[2]}\nPosition: {employee[3]}\nSalary: {employee[4]}\n")

cnx.commit()
cursor.close()
cnx.close()
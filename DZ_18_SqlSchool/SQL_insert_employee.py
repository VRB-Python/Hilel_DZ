import mysql.connector
cnx = mysql.connector.connect(user="root", password="1111", database="Bodnar_school")
cursor = cnx.cursor()


add_employee = ("INSERT INTO employees "
                "(emp_id, first_name, last_name, position, salary) "
                "VALUES (%s,%s, %s, %s, %s)")

data_employee = ( (1, "Adam", "Smith", "Director", 5000), (2, "Eva", "Loom", "English teacher", 3500),  (3, "John", "Karter", "Math teacher", 3500))
for emp in data_employee:
    cursor.execute(add_employee, emp)
    
# Якщо потрібно додати одного то можна так:
#data_employee = (1, "Adam", "Smith", "Director", 5000)
#cursor.execute(add_employee, data_employee)

cnx.commit()
cursor.close()
cnx.close()
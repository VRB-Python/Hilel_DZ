import mysql.connector

cnx = mysql.connector.connect(user="root", password="1111", database="Bodnar_school")
cursor = cnx.cursor()

add_class = ("INSERT INTO class"
                  "(class_id, class_name, classmate_id)"
                  "Values (%s, %s, %s)")

data_class = ((1, "1 - A", 2), (2, "1 - B", 3))
for t in data_class:
    cursor.execute(add_class, t)

# Якщо потрібно додати один клас то можна так:
# data_class = (3, "1 - C", 1)
# cursor.execute(add_class, data_class)

cnx.commit()
cursor.close()
cnx.close()
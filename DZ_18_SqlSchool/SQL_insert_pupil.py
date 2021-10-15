import mysql.connector

cnx = mysql.connector.connect(user="root", password="1111", database="Bodnar_school")
cursor = cnx.cursor()

add_pupil = ("INSERT INTO pupils"
                  "(pupil_id, first_name, last_name, pupil_class_id)"
                  "Values (%s, %s, %s, %s)")

data_pupil = ((1, "Oksana", "Chorna", 2), (2, "Nick", "Corleone", 2), (5, "Jack", "Forester", 1), (4, "Nelly", "Furtado", 1 ))
for pupe in data_pupil:
    cursor.execute(add_pupil, pupe)

# Якщо потрібно одного учня то можна так:
# data_pupil = (3, "Dave", "Bilyk", 2)
# cursor.execute(add_pupil, data_pupil)

cnx.commit()
cursor.close()
cnx.close()
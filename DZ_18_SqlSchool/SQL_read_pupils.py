import mysql.connector

cnx = mysql.connector.connect(user="root", password="1111", database="Bodnar_school")
cursor = cnx.cursor()

query_pupils = ("SELECT * from pupils")

cursor.execute(query_pupils)
all_pupils = cursor.fetchall()

for pupil in all_pupils:
    print(f"Id: {pupil[0]}\nName: {pupil[1]} {pupil[2]}\nClass_ID: {pupil[3]}\n")

cnx.commit()
cursor.close()
cnx.close()
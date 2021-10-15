import mysql.connector

cnx = mysql.connector.connect(user="root", password="1111", database="Bodnar_school")
cursor = cnx.cursor()

query_class = ("SELECT * from class")

cursor.execute(query_class)
all_classes = cursor.fetchall()

for group in all_classes:
    print(f"Id: {group[0]}\nName: {group[1]}\nClassmate_ID: {group[2]}\n")

cnx.commit()
cursor.close()
cnx.close()
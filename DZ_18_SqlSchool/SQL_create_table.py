import mysql.connector

DB_NAME = 'Bodnar_school'

TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_id` int(11) NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `position` varchar(50) NOT NULL,"
    "  `salary` int, "
    "  PRIMARY KEY (`emp_id`)"
    ") ENGINE=InnoDB")

TABLES['class'] = (
    "CREATE TABLE `class` ("
    "  `class_id` int NOT NULL,"
    "  `class_name` varchar(40) NOT NULL,"
    " `classmate_id` int NOT NULL,"
    "  PRIMARY KEY (`class_id`), "
    " foreign key (`classmate_id`) "
    " references `employees` (`emp_id`) "
    ") ENGINE=InnoDB")

TABLES['pupils'] = (
    "CREATE TABLE `pupils` ("
    "  `pupil_id` int NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `pupil_class_id` int NOT NULL,"
    "  PRIMARY KEY (`pupil_id`),"
    " foreign key (`pupil_class_id`) references `class` (`class_id`) "
    ") ENGINE=InnoDB")

cnx = mysql.connector.connect(user = "root", password = "1111")
cursor =cnx.cursor()
cnx.database = DB_NAME
for table_name in TABLES:
    table_description = TABLES[table_name]
    print(f"Create table {table_name}")
    cursor.execute(table_description)
cursor.close()
cnx.close()

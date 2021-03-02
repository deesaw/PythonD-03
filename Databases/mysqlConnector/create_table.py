

from mysql.connector import connection
from mysql.connector import errorcode
DB_NAME = 'pydbE1x'
cnx = connection.MySQLConnection(user='root', password='hello123',host='127.0.0.1',
                                 database=DB_NAME)
mycursor=cnx.cursor()
#mycursor.execute("USE {}").format(DB_NAME)

TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ")" )

TABLES['departments'] = (
    "CREATE TABLE `departments` ("
    "  `dept_no` char(4) NOT NULL,"
    "  `dept_name` varchar(40) NOT NULL,"
    "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
    ") ")

for name in TABLES:
          
          mycursor.execute(TABLES[name])
          print("Created table",name)


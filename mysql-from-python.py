import os
import pymysql

#Get Username from GitPod Workspace
#(Modify this varible if running on another enviornment)

username = os.getenv('C9_USER')

#Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    with connection.cursor() as cursor:
        names = ["jim", "bob"]
        cursor.execute("DELETE FROM Friends WHERE name in ("%s", "%s")", names)
        connection.commit()
finally:
    connection.close()
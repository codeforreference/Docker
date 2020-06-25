from time import gmtime, strftime
import mysql.connector
import os
conx = mysql.connector.connect(host='app-db',database='appdb',user='root',password='welcome*123')
currenttime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
hostname = os.getenv('HOSTNAME')
hostip = os.getenv('IP_ADDRESS')
if conx.is_connected():
    db_info = conx.get_server_info()
    print("Connected to MySQL Server ", db_info)
    table_query = """CREATE TABLE IF NOT EXISTS `hostdata` (
                Time varchar(25) NOT NULL, 
                HostName varchar(250) NOT NULL, 
                HostIP varchar(20) NOT NULL) """
    insert_query = """INSERT INTO hostdata (Time, HostName, HostIP)
                      VALUES (%s, %s, %s)"""
    dataTuple = (currenttime, hostname, hostip)
    cursor = conx.cursor()
    cursor.execute(table_query)
    cursor.execute(insert_query, dataTuple)
    conx.commit()
    cursor.close()
    conx.close()
    print("Successfully updated the data into mysql database")
else:
    print("Can't connect to MySQL Database")
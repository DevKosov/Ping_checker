import mysql.connector # imported mysql library to connect with python
import math # imported math to round the ping
from pythonping import ping # pythonping library makes it possible to ping with python
from time import sleep # the timeout
from datetime import datetime # the current time

mydb = mysql.connector.connect( # python connect to mysql
    host='localhost', # into the host in my case localhost
    user='root', # with the username root
    password='admin', # with the password admin
    database='ping', # it connects to the database 'ping'
)

my_cursor = mydb.cursor() #making a variable of database cursor so i can work faster

while True:

    nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # current time

    response_list = ping('8.8.8.8', size=32, count=1) # pinging 8.8.8.8 once (only once because i dont want too much overflow)

    the_ping = round(response_list.rtt_avg_ms) # rounded the ping ex 28.1 rounded to 28

    if the_ping >= 120 : #if the ping is higher or equal to 120 execute code below
        print(nowtime,': Your Internet is not working correctly. Your ping is %dms.' % the_ping) # print the current ping

        my_cursor.execute('INSERT INTO ping_results (ping) VALUES(%d);' % the_ping) # Insert in to ping_results table the current ping
        my_cursor.execute('DELETE FROM ping_results WHERE the_time < NOW() - INTERVAL 1 DAY;') # Delete the data from ping_results if they are older than 1 day for limited storage
        mydb.commit() # This sends a COMMIT statement to the MySQL server.

        reload_time = 10 # more frequent ping checks if the ping is higher than 120. In this case every 10 seconds

    elif the_ping >= 2000 :
        print(nowtime,': Your Internet is not working!! Your ping returns a timeout!!') # print the current ping

        my_cursor.execute('INSERT INTO ping_results (ping) VALUES(%d);' % the_ping) # Insert in to ping_results table the current ping
        my_cursor.execute('DELETE FROM ping_results WHERE the_time < NOW() - INTERVAL 1 DAY;') # Delete the data from ping_results if they are older than 1 day for limited storage
        mydb.commit()   # This sends a COMMIT statement to the MySQL server.
    else: #Else if the ping is lower than 120 execute code below
        print(nowtime,': Your Internet is working. Your ping is %dms.' % the_ping) # print the current ping

        my_cursor.execute('INSERT INTO ping_results (ping) VALUES(%d);' % the_ping) # Insert in to ping_results table the current ping
        my_cursor.execute('DELETE FROM ping_results WHERE the_time < NOW() - INTERVAL 1 DAY;') # Delete the data from ping_results if they are older than 1 day for limited storage
        mydb.commit() # This sends a COMMIT statement to the MySQL server.

        reload_time = 60 # less frequent ping checks if the ping is lower than 120. In this case every 60 seconds
    sleep(reload_time)
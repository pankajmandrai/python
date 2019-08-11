#import pyodbc

#conn_str = (r'DRIVER={SQL Server};'r'SERVER=(local)\SQLEXPRESS;'r'DATABASE=myDb;'r'Trusted_Connection=yes;')
#cnxn = pyodbc.connect(conn_str)
#print("success")


import pyodbc

host = "XX.XX.XXX.XX"
database = "myDB"
username = "dtinnxx"
password = "password"

print ("DB CONNECT ATTEMPT")
try:
    cs = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (host, username, password, database)
    cnxn = pyodbc.connect(cs)
    print ("SUCCESS")
except Exception as e:
    print ("Error: " + str(e))

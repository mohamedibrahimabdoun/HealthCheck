import mail_management as mailobj
import file_managment as fileobj
import cx_Oracle
import  pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import db_management as db
import MySQLdb
import pyodbc
import datetime as dt

thisday=dt.date.today()
subject= 'HealthCheck - %s' %thisday.strftime("%B %d")
#dt.strftime(thisday,'%m/%d/%Y')
print subject 

#sqlsever_obj=db.db_management("ebus","zain@123","172.22.2.116\SPPDB","","")
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=172.22.2.116\SPPDB;DATABASE=;UID=ebus;PWD=zain@123')
try:
    
 
    data = pd.read_sql("select * from zainportal.dbo.HealthCheck_SuccessfulUserTransactions", cnxn)
    print type(data)
   
except  Exception,e : print Exception.args,e
finally:
    cnxn.close()
import mail_management as mailobj
import file_managment as fileobj
import cx_Oracle
import  pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import db_management as db
import datetime as dt


'''
attachments=[]
fromlist=[]
tolist=["mohamed.osman@bh.zain.com"]
attachments=fileobj.getdirectoryfile("C:\HealthCheck\SQL")
#print attachments

flag = mailobj.send_mail( "mohamed.osman@bh.zain.com" ,tolist, "Test", "PFA",attachments, "mail.bh.zain.com")
'''

attachments=fileobj.getdirectoryfile("C:\HealthCheck\SQL")

Oracledb_obj=db.db_management("osman$","osman_2016","172.22.2.108","1525", "WOWDB")
mysqldb_obj=db.db_management("zainadmin","mobapps","172.22.3.217","3306", "selfcare")
sqlsever_obj=db.db_management("ebus","zain@123","172.22.2.116\SPPDB","","")

writer = pd.ExcelWriter("C:\HealthCheck\Output\HealthCheck.xlsx",engine='xlsxwriter',datetime_format='dd-mmm-yyyy',date_format='mmmm dd yyyy')



df_HC_BUNDLE_SUCCESS_TRANSACTIONS=Oracledb_obj.getDataFramefromOracleQuery("SELECT * FROM OSMAN$.HC_BUNDLE_SUCCESS_TRANSACTIONS")
df_HC_BUNDLE_SUCCESS_TRANSACTIONS.pivot('INSERT_DATE','STATUS','COUNT_').to_excel(writer, "BUNDLE_SUCCESS_TRANSACTIONS",na_rep=0)


df_HC_NRA_AVG_RESPONSE_TIME=Oracledb_obj.getDataFramefromOracleQuery("SELECT * FROM OSMAN$.HC_NRA_AVG_RESPONSE_TIME")
df_HC_NRA_AVG_RESPONSE_TIME.pivot('HOURS','DATE_','COUNT_').to_excel(writer, "NRA_AVG_RESPONSE_TIME",na_rep=0)


df_HC_NRA_SUCCESS_FAILED_TRANS=Oracledb_obj.getDataFramefromOracleQuery("select * from OSMAN$.HC_NRA_SUCCESS_FAILED_TRANS")
pd.pivot_table(df_HC_NRA_SUCCESS_FAILED_TRANS,values='CNT',index=['STATUS','HR'],columns=['DATE_'],aggfunc='sum').to_excel(writer, "NRA_SUCCESS_FAILED_TRANS",na_rep=0)


df_HC_NRA_SUCCESS_PER_CHANNAL=Oracledb_obj.getDataFramefromOracleQuery("select * from OSMAN$.HC_NRA_SUCCESS_PER_CHANNAL")
pd.pivot_table(df_HC_NRA_SUCCESS_PER_CHANNAL,values='COUNT_',index=['HRS'],columns=['DATE_','ACTIVATION_METHOD'],aggfunc='sum').to_excel(writer, "NRA_SUCCESS_PER_CHANNAL",na_rep=0)

#select * from HC_Subscribers_Logins

df_HC_MobileAPP_Subscribers_Logins=mysqldb_obj.getDataFramefromMYSQLQuery("select * from HC_Subscribers_Logins")
df_HC_MobileAPP_Subscribers_Logins.to_excel (writer, "MobileAPP_Subscribers_Logins",na_rep=0)

df_Portal_SuccessfulUserTransactions=sqlsever_obj.getDataframefromMS_SQL("select * from zainportal.dbo.HealthCheck_SuccessfulUserTransactions")
pd.pivot_table(df_Portal_SuccessfulUserTransactions,values='cnt',index=['date_'],columns=['FaultCode'],aggfunc='sum').to_excel (writer, "Portal_UserTransactions",na_rep=0)


writer.save()
print('Done')

#Output.xlsx
thisday=dt.date.today()
subject= 'HealthCheck - %s' %thisday.strftime("%B %d")
print subject
files=fileobj.getdirectoryfile("C:\HealthCheck\Output")
#msg = 'Subject: %s\n\n%s' % (subject, "PFA")
mailobj.send_mail('mohamed.osman@bh.zain.com', ['mohamed.osman@bh.zain.com','Taqi.Kabeer@bh.zain.com','Nasreen.Shablaq@bh.zain.com'], subject, "Please Find attached File", files, "mail.bh.zain.com")
print('emailSend')


#mysqldb_obj=db.db_management("zainadmin","mobapps","172.22.3.217","3306", "selfcare")



import mail_management as mailobj
import file_managment as fileobj
import cx_Oracle
import MySQLdb
import  pandas as pd
import pyodbc





class db_management(object):


    def __init__(self,username,passwrd,ip,port,dbname):
        self.username=username
        self.passwrd=passwrd
        self.ip=ip
        self.port=port
        self.dbname=dbname
        

    def getDataFramefromOracleQuery(self,SQL):
        '''
        This function will return DataFrame from a query you pass
        ''' 
        dsnStr = cx_Oracle.makedsn(self.ip, self.port, self.dbname)
        con = cx_Oracle.connect(self.username,self.passwrd,dsnStr)
        try :
            print dsnStr
            c=con.cursor()
            c.execute(SQL)
            names = [x[0]for x in c.description]
            #print(list(c.description))
        
            rows = c.fetchall()
            df=pd.DataFrame( rows, columns=names)
            return df
        except Exception: 
            pass
        finally:
            con.close()
            
            
    def getDataFramefromMYSQLQuery(self,SQL):
        db = MySQLdb.connect(host=self.ip, user=self.username, passwd=self.passwrd,db=self.dbname)
        try :
            cn=db.cursor()
            cn.execute(SQL)
            names = [x[0]for x in cn.description]
            rows =cn.fetchall()
            df=pd.DataFrame( list(rows), columns=names)
            return df
        except Exception,e: print Exception, e
        finally:
            db.close()
    
    def getDataframefromMS_SQL(self,SQL):
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' %(self.ip,self.dbname,self.username,self.passwrd))
        try:
            
         
            data = pd.read_sql(SQL, cnxn)
            return data
           
        except  Exception,e : print Exception.args,e
        finally:
            cnxn.close()
            
            
        



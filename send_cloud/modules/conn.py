
import psycopg2
import json
import sqlite3
import os 
import pandas as pd



class ODBC:
    
    def __init__(self, path, type_sgdb):
        
        
        self.path = path
        
        self.config = json.loads(open(str(self.path) + '/send_cloud/modules/conn_settings.json').read())
        
        
        if type_sgdb=='POSTGRE_DEV':
            
            self.host      =  self.config['SGDBS']['POSTGRE_DEV']['HOST']
            self.database  =  self.config['SGDBS']['POSTGRE_DEV']['DB']
            self.user      =  self.config['SGDBS']['POSTGRE_DEV']['USER']
            self.password  =  self.config['SGDBS']['POSTGRE_DEV']['PWD']
            
        
        else:
            raise Exception("SGDB don't exist on settings")
            
            
    def open_con(self):
            
        self.con = psycopg2.connect(host      =  self.host, 
                                    database  =  self.database, 
                                    user      =  self.user,
                                    password  =  self.password)

        return self.con
    
    def close_con(self):
        self.con.close()




class SQLITE:
    
    def __init__(self, path, name_db):
        
        self.path = path
        
        self.name_db = name_db
    
    def read(self, query):
            
        with sqlite3.connect(os.path.join(self.path, "local_data", self.name_db)) as connection:
                            
            return pd.read_sql(sql=query, con=connection)

            
            
    def execute(self, query):
        
        
        with sqlite3.connect(os.path.join(self.path, "local_data", self.name_db)) as connection:
            
           
            cur = connection.cursor()
            
                      
            cur.execute(query)
            connection.commit()
                

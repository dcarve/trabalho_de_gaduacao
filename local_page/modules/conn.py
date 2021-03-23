
import sqlite3
import os 
import pandas as pd





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
                

import sqlite3
import os 
import pandas as pd


class SQLITE:
    
    def __init__(self, path,  name_db):
        
        self.name_db = name_db
        self.path = path
    
    def read(self, query):
                
        with sqlite3.connect(os.path.join(self.path, "local_data", self.name_db)) as connection:
                            
            return pd.read_sql(sql=query, con=connection)
                

        
    
    def insert(self, dictionary):
        
        with sqlite3.connect(os.path.join(self.path, "local_data", self.name_db)) as connection:
                            

            
            table = dictionary['table']
            list_inserts = dictionary['data']
            
            for insert in list_inserts:
                columns = ', '.join(['"'+key+'"' for key in insert])
                values = ', '.join(["'"+insert[key]+"'" if type(insert[key])==str else str(insert[key]) for key in insert])
                
                query = f"""insert into {table} (
                    {columns} )
                values
                ( {values}
                )"""
                
                
                cur = connection.cursor()
                
                cur.execute(query)
                
                cur.close()
                
                connection.commit()
                
 
                
            

    def update(self):
        pass
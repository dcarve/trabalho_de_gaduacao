import pandas as pd

try:

    from modules.conn import SQLITE

except:
    
    from send_cloud.modules.conn import SQLITE
    
    

def record_measure(path, _odbc):
    

    con = _odbc.open_con()
    
    data_cloud  = pd.read_sql('select * from tg.measure_system limit 1', con)
    
    if data_cloud.empty:
        

    
        new_data = SQLITE(path, 'data.db').read(f"""select 
                                                  "'"||sensor_cod||"'" as sensor_cod, 
                                                  "values", 
                                                  event_timestamp    
                                            from sensors""")
     
    else:
        
    
        last_event_timestamp_cloud = str(pd.read_sql('select max(event_timestamp) as last_event_timestamp from tg.measure_system', con)['last_event_timestamp'].max())
    

        
        new_data = SQLITE(path, 'data.db').read(f"""select 
                                                  "'"||sensor_cod||"'" as sensor_cod, 
                                                  "values", 
                                                  event_timestamp    
                                            from sensors where event_timestamp > {last_event_timestamp_cloud}""")
        
        
    
    if new_data.empty:
        
        pass
    
    else:
        
        lista = "(" + new_data['sensor_cod'] + ', ' + new_data['values'].astype(str) + ', ' + new_data['event_timestamp'].astype(str) +  ")"
        
        lista = ','.join(lista)
        
        
        cur = con.cursor()
        
        sql = f"""insert into tg.measure_system values {lista}"""
                   
        cur.execute(sql)
        con.commit()
        
        _odbc.close_con()
        
        
        
        last_event_timestamp_local = new_data['event_timestamp'].max()
        
        SQLITE(path, 'data.db').execute(f"""delete from  sensors where event_timestamp<= {last_event_timestamp_local}""")
            
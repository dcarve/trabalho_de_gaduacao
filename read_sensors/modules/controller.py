
from random import seed
from random import randint
import time



try:
    from modules.conn import SQLITE

except:
    from read_sensors.modules.conn import SQLITE

seed(1)


class SENSORS:
    
    def __init__(self, path, list_slots, sensor_name_slot):
        
        self.list_slots = list_slots
        self.sensor_name_slot = sensor_name_slot
        self.path = path


              

    def __SLOT_1__(self):
        
        res = {"values": randint(0, 1000)/10, 
               "event_timestamp": int(time.time())}
        
        return res
    
    
    def __SLOT_2__(self):
        
        res = {"values": randint(0, 1000)/10, 
               "event_timestamp": int(time.time())}
        
        return res
    
    def __SLOT_3__(self):
        
        res = {"values": randint(0, 1000)/10, 
               "event_timestamp": int(time.time())}
        
        return res
    
    def __SLOT_4__(self):
        
        res = {"values": randint(0, 1000)/10, 
               "event_timestamp": int(time.time())}
        
        return res
    
    
    
    
    def read_sensors(self):
        
        lista_res = []
        
        for slot in self.list_slots:
            
            if slot == 'SLOT_1':
                
                res = self.__SLOT_1__()
                res['sensor_cod'] = self.sensor_name_slot[slot]
                
                lista_res.append(res)
            
            elif slot == 'SLOT_2':
                
                res = self.__SLOT_2__()
                res['sensor_cod'] = self.sensor_name_slot[slot]
                
                lista_res.append(res)
            
            
            elif slot == 'SLOT_3':
                
                res = self.__SLOT_3__()
                res['sensor_cod'] = self.sensor_name_slot[slot]
                
                lista_res.append(res)
            
            
            elif slot == 'SLOT_4':
                
                res = self.__SLOT_4__()
                res['sensor_cod'] = self.sensor_name_slot[slot]
                
                lista_res.append(res)
            
                

        SQLITE(self.path, 'data.db').insert( {
        	"table":"sensors",
        	"data":lista_res
        })
    


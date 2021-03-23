import time
import json
import os
from pathlib import Path

try:
    
    from modules.conn import SQLITE
    from modules.controller import SENSORS
    
    primary_path = Path().absolute().parent

except:

    from read_sensors.modules.conn import SQLITE
    from read_sensors.modules.controller import SENSORS
    
    primary_path = Path().absolute()


def thread_main():


    print("Run machine...")
    print("reading sensors...")
    
    
    while True:
        
        _sqlite_config = SQLITE(primary_path, 'config.db')

        sensor_name_slot = _sqlite_config.read("""select '"' || slot || '":"' || sensor_cod || '"' as slots from sensors_description""")['slots'].to_list()
        sensor_name_slot  = "{"+ ",".join(sensor_name_slot) + "}"
        sensor_name_slot = json.loads(sensor_name_slot)
        
        
        list_slots = _sqlite_config.read("""select slot from sensors_description where "on" = 1""")['slot'].to_list()

        
        SENSORS(primary_path, list_slots, sensor_name_slot).read_sensors()
        
        time.sleep(30)


   
    

if __name__ == "__main__":
    

    clear = lambda: os.system('cls')
    clear()
    
    
    thread_main()





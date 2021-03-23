import time
import os
from pathlib import Path


try:
    
    from modules.conn import ODBC
    from modules import send
    
    primary_path = Path().absolute().parent
    
except:
    
    from send_cloud.modules.conn import ODBC
    from send_cloud.modules import send
    
    primary_path = Path().absolute()
    


def thread_main():

    print("run sender cloud ...")
    
    
    _odbc = ODBC(primary_path, 'POSTGRE_DEV')
    
    while True:
        
        send.record_measure(primary_path, _odbc)
        time.sleep(30)



    
if __name__ == "__main__":

    clear = lambda: os.system('cls')
    clear()
    

    thread_main()
    

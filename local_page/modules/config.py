from modules.conn import SQLITE
from pathlib import Path   

path = Path().absolute().parent


class CONFIG:
    
    
    def __init__(self, **kwards):
        
        self.SLOT_1 = {}
        self.SLOT_2 = {}
        self.SLOT_3 = {}
        self.SLOT_4 = {}


    
    def get_data_config(self):
        

        
        data = SQLITE(path, 'config.db').read(f"""select *   
                                            from sensors_description""")
    
        
        
        ##SLOT 1
        self.SLOT_1['name_slot'] = data.loc[data.slot == 'SLOT_1']['sensor_cod'].max()
        self.SLOT_1['decription'] = data.loc[data.slot == 'SLOT_1']['sensor_description'].max()
        
        
        if data.loc[data.slot == 'SLOT_1']['on'].max()==1:
            self.SLOT_1['read'] = 'checked'
        else:
            self.SLOT_1['read'] = ''
            
            
        ##SLOT 2
        self.SLOT_2['name_slot'] = data.loc[data.slot == 'SLOT_2']['sensor_cod'].max()
        self.SLOT_2['decription'] = data.loc[data.slot == 'SLOT_2']['sensor_description'].max()
        
        
        if data.loc[data.slot == 'SLOT_2']['on'].max()==1:
            self.SLOT_2['read'] = 'checked'
        else:
            self.SLOT_2['read'] = ''
            
            
        ##SLOT 3
        self.SLOT_3['name_slot'] = data.loc[data.slot == 'SLOT_3']['sensor_cod'].max()
        self.SLOT_3['decription'] = data.loc[data.slot == 'SLOT_3']['sensor_description'].max()
        
        
        if data.loc[data.slot == 'SLOT_3']['on'].max()==1:
            self.SLOT_3['read'] = 'checked'
        else:
            self.SLOT_3['read'] = ''
            
            
        ##SLOT 4
        self.SLOT_4['name_slot'] = data.loc[data.slot == 'SLOT_4']['sensor_cod'].max()
        self.SLOT_4['decription'] = data.loc[data.slot == 'SLOT_4']['sensor_description'].max()
        
        
        if data.loc[data.slot == 'SLOT_4']['on'].max()==1:
            self.SLOT_4['read'] = 'checked'
        else:
            self.SLOT_4['read'] = ''
           
            
        
    def update_info(self, **kwards):
        slot = kwards.get('slot')
        
        if slot:
            
            name_slot = kwards.get('name_slot')
            description = kwards.get('description')
            read = kwards.get('read')
            
            print(slot)
            print(read)

            if name_slot:
                SQLITE(path, 'config.db').execute(f"""update sensors_description set sensor_cod = '{name_slot}' where slot='{slot}'""")

            if description:
                SQLITE(path, 'config.db').execute(f"""update sensors_description set sensor_description = '{description}' where slot='{slot}'""")

            if read or read==0:
                print(f"""update sensors_description set 'on'={read} where slot='{slot}'""")
                SQLITE(path, 'config.db').execute(f"""update sensors_description set 'on'={read} where slot='{slot}'""")

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
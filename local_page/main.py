
from flask import Flask
from flask import render_template, request


from modules.config import CONFIG
    



app = Flask(__name__)


_config = CONFIG()
        




@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
    
        name_slot_1             = request.form['name_slot_1']
        description_slot_1      = request.form['description_slot_1']


        if 'read_slot_1' in request.form:
            read_slot_1 = 1
        else:
            read_slot_1 = 0
        
        _config.update_info(slot            = 'SLOT_1',
                            name_slot       = name_slot_1, 
                            description     = description_slot_1, 
                            read            = read_slot_1)
        
        
        
    
        name_slot_2             = request.form['name_slot_2']
        description_slot_2      = request.form['description_slot_2']
        
        if 'read_slot_2' in request.form:
            read_slot_2 = 1
        else:
            read_slot_2 = 0
        
        _config.update_info(slot            = 'SLOT_2',
                            name_slot       = name_slot_2, 
                            description     = description_slot_2, 
                            read            = read_slot_2)
        
        
        
        
    
        name_slot_3             = request.form['name_slot_3']
        description_slot_3      = request.form['description_slot_3']
        
        if 'read_slot_3' in request.form:
            read_slot_3 = 1
        else:
            read_slot_3 = 0
        
        _config.update_info(slot            = 'SLOT_3',
                            name_slot       = name_slot_3, 
                            description     = description_slot_3, 
                            read            = read_slot_3)
        
        
        
        
    
        name_slot_4             = request.form['name_slot_4']
        description_slot_4      = request.form['description_slot_4']
        
        if 'read_slot_4' in request.form:
            read_slot_4 = 1
        else:
            read_slot_4 = 0
        
        _config.update_info(slot            ='SLOT_4',
                            name_slot       = name_slot_4, 
                            description     = description_slot_4, 
                            read            = read_slot_4)
        
        


        
        _config.get_data_config()
        
        return render_template('index.html', 
                                name_slot_1         = _config.SLOT_1['name_slot'],
                                description_slot_1  = _config.SLOT_1['decription'],
                                read_slot_1         = _config.SLOT_1['read'], 
                                
                                name_slot_2         = _config.SLOT_2['name_slot'],
                                description_slot_2  = _config.SLOT_2['decription'],
                                read_slot_2         = _config.SLOT_2['read'],
                                
                                name_slot_3         = _config.SLOT_3['name_slot'],
                                description_slot_3  = _config.SLOT_3['decription'],
                                read_slot_3         = _config.SLOT_3['read'],
                                
                                name_slot_4         = _config.SLOT_4['name_slot'],
                                description_slot_4  = _config.SLOT_4['decription'],
                                read_slot_4         = _config.SLOT_4['read'])    
        
    
    else:

        
        _config.get_data_config()
        
        return render_template('index.html', 
                                name_slot_1         = _config.SLOT_1['name_slot'],
                                description_slot_1  = _config.SLOT_1['decription'],
                                read_slot_1         = _config.SLOT_1['read'], 
                                
                                name_slot_2         = _config.SLOT_2['name_slot'],
                                description_slot_2  = _config.SLOT_2['decription'],
                                read_slot_2         = _config.SLOT_2['read'],
                                
                                name_slot_3         = _config.SLOT_3['name_slot'],
                                description_slot_3  = _config.SLOT_3['decription'],
                                read_slot_3         = _config.SLOT_3['read'],
                                
                                name_slot_4         = _config.SLOT_4['name_slot'],
                                description_slot_4  = _config.SLOT_4['decription'],
                                read_slot_4         = _config.SLOT_4['read'])


if __name__ == '__main__':

    app.run(debug=True)
from os import path, remove
from pickle import dump, load

from web.backend.local.dbOperations import DataBase
from web.backend.table_chose import TableChose
from web.backend.local.error import *

import eel

class Connect:

    #инициализация и все такое
    def __init__(fles):
        Connect.load()

    @eel.expose
    def take_data(data, is_on):
        if is_on == "on":
            Connect.save(data)
        else:
            with open('web/backend/user/user.pkl', 'wb') as file: 
                remove(file)
        
        try:   
            db = DataBase(data[0], data[1], data[2], data[3])
        except LoginError as e:
            eel.alert_c("Не удалось войти! Проверьте данные для входа.")
            return False

        else:
            eel.btl.response.set_cookie('is_connected', 'True')
            TableChose(db)
            return True
 
    def save(data):
        if not path.exists('web/backend/user/user.pkl'):
            a = open('web/backend/user/user.pkl', 'w')
            a.close()
        
        with open('web/backend/user/user.pkl', 'wb') as file:        
            dump(data, file)
        
    def load():
        if path.exists('web/backend/user/user.pkl'):
            with open('web/backend/user/user.pkl', 'rb') as f:
                data = load(f)
                if not data:
                    return 1
                
                else:
                    eel.set_data(data)
        else:
            return 1
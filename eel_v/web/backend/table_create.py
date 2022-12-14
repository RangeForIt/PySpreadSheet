from web.backend.local.dbOperations import DataBase
from mysql.connector.errors import DatabaseError

import eel

class TableCreate:
    def __init__(self, db : DataBase):
        TableCreate.db = db
    
    @eel.expose
    def create_table(table_data):
        if eel.btl.request.get_cookie('is_connected') == None:
            eel.go_to_connect()
        else:
            pass
         
        query = f'create table {table_data[0]}('
        
        for col in table_data[1]:
            if col[1] == 'varchar':
                query += f'{col[0]} {col[1]}({table_data[2]}) '
            else:
                query += f'{col[0]} {col[1]} '
                
            for param in col[2]:
                query += ' ' + param
            
            if col != table_data[1][-1]:
                query += ', '
        
        query += ');'
        
        if TableCreate.test_for_error(TableCreate.db.make_command(query, True)):
            print('a')
            eel.alert_create('Таблица была создана некорректно!')
        else:
            print('b')
            eel.alert_create('Таблица создана!')
            
        eel.go_to_tch()

    def test_for_error(exp):#проверка на ошибку
        if DatabaseError in type(exp).__bases__:
            return True
    
        else:
            return False
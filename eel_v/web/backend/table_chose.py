from web.backend.table_edit import Editor
from web.backend.local.dbOperations import DataBase
from web.backend.local.execute_command import Execute
from web.backend.table_create import TableCreate

import eel

class TableChose:

    #инициализация
    def __init__(fles, db : DataBase):
        TableChose.db = db
    
    @eel.expose
    def load_tables():
        if eel.btl.request.get_cookie('is_connected') == None:
            eel.go_to_connect()
            print('a')
        else:
            pass
        
        eel.add_table(TableChose.db.make_command(f'select table_name from information_schema.tables where table_schema = "{TableChose.db.db}";', False))
    
    @eel.expose
    def open_table(name):
        Editor(TableChose.db, name)
    
    @eel.expose
    def make_command(command):
        Execute(TableChose.db).handle(command)
    
    @eel.expose
    def create_instance_c():
        TableCreate(TableChose.db)
    
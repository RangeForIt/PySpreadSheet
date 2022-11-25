from web.backend.local.dbOperations import DataBase

import eel

class Instance:#для выовда селекта
    def __init__(fels, db : DataBase, command):
        Instance.db = db
        Instance.result = db.make_command(command, False)
    
    @eel.expose
    def show_r():
        eel.load_tables_inst(Instance.result)

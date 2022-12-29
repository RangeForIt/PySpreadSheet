from web.backend.local.dbOperations import DataBase
from mysql.connector.errors import OperationalError, ProgrammingError

import eel

class Instance:#для выовда селекта
    def __init__(fels, db : DataBase, command):
        Instance.db = db
        Instance.result = db.make_command(command, False)
        
    @eel.expose
    def show_r():
        if eel.btl.request.get_cookie('is_connected') == None:
            eel.go_to_connect()
        else:
            pass
        
        if type(Instance.result) == OperationalError or type(Instance.result) == ProgrammingError:
            eel.show_error()
            return 1
        else:
            eel.load_tables_inst(Instance.result)

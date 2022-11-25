from web.backend.table_instance import Instance
from web.backend.local.dbOperations import DataBase

import eel

class Execute:

    #инициализация
    def __init__(self, db : DataBase):
        self.db = db
    
    def handle(self, command):
        if command.startswith('select'):#если начинается с селект
            Instance(self.db, command)
            eel.go_inst()
        
        elif command.startswith('drop'):#если начинается с дроп
            if eel.ask('Вы собираетесь что-то удалить. Вы уверены?')():
                self.db.make_command(command, True)
                eel.reload()

            else:
                return 0
        
        else:#если команда-ноунейм
            res = self.db.make_command(command, True)
            eel.alrt(res)
            eel.reload()
            
        return 0
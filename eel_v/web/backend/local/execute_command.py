from web.backend.table_instance import Instance
from web.backend.local.dbOperations import DataBase
from mysql.connector.errors import ProgrammingError

import eel

class Execute:

    #инициализация
    def __init__(self, db : DataBase):
        self.db = db
    
    def handle(self, command):
        print(command)
        if command.lower().startswith('select'):#если начинается с селект
            Instance(self.db, command)
            eel.go_inst()
        
        elif command.lower().startswith('drop'):#если начинается с дроп
            if eel.ask('Вы собираетесь что-то удалить. Вы уверены?')():
                res = self.db.make_command(command, True)
                if type(res) == ProgrammingError:
                    eel.alrt("Ошибка! Результат - " + str(res))
                    eel.reload()
                    return 1
                eel.reload()

            else:
                return 0
        
        else:#если команда-ноунейм
            res = self.db.make_command(command, True)
            if type(res) == ProgrammingError:
                    eel.alrt("Ошибка! Результат - " + str(res))
                    eel.reload()
                    return 1
            eel.alrt("Успешно! Результат - " + str(res))
            eel.reload()
            
        return 0
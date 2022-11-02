from tkinter import *
from tkinter import messagebox
from table_actions.table_instance import GUI as g

class GUI():

    #инициализация
    def __init__(self, db, db_name):
        self.db = db
        self.name = db_name
    
    def main(self, command, obj):
        if command.startwith('select'):#если начинается с селект
            g(self.db, self.db.make_command(command + ';', False), command)
            return 0
        
        elif command.startwith('drop'):#если начинается с дроп
            if messagebox.askokcancel("Вы уверены?", 'Вы собираетесь что то удалить. Вы уверены?'):
                messagebox.showinfo('Выход', str(self.db.make_command(command + ';', False)))

            else:
                return 0
        
        else:#если команда-ноунейм
            messagebox.showinfo('Выход', str(self.db.make_command(command + ';', False)))
    
        obj.update()#обновление экрана тейбл чоуза

        return 0
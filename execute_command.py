from tkinter import *
from tkinter import messagebox
from common.com import Scheme
from table_actions.table_instance import GUI as g

class GUI(Scheme):

    def __init__(self, db, db_name):
        self.db = db
        self.name = db_name

        self.primary()

    def primary(self):
        pass
    
    def main(self, command, obj):
        data_scheme = command.split(' ')

        if data_scheme[0] == 'select':
            g(self.db, self.db.make_command(command + ';', False), command)
            return 0
        
        elif data_scheme[0] == 'drop':
            if messagebox.askokcancel("Вы уверены?", 'Вы собираетесь что то удалить. Вы уверены?'):
                super().__init__('Response')
                ret = self.db.make_command(command + ';', True)
                message = Label(self.root_w, text=ret)
                message.grid(column=0, row=0)

            else:
                return 0
        
        else:
            super().__init__('Response')
            ret = self.db.make_command(command + ';', True)
            message = Label(self.root, text=ret)
            message.grid(column=0, row=0)
    

        obj.update()

        pass
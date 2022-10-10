from tkinter import *

from table_actions.table_handler import Handler
from common.com import Scheme

class GUI(Scheme):
    def __init__(self, db, result, command):
        super().__init__('Response', with_scroll=True)
        self._table = command.split()[-1]
        self._result = result
        self._handler = Handler(db, self._table)

        self._rows = len(self._result)#кол-во строк
        self._cols = len(self._result[0])#кол-во колонок

        self._types = self._handler.col_types#типы колонок
        self._type_lables = []#массив лейблов колонок
        
        #приминение функций
        self.primary()
        self.main()
    
    def primary(self):
        for i in range(len(self._types)):
            self._type_lables.append(Label(self.root_f, text=self._types[i]))
            self._type_lables[-1].grid(column=i, row=0)
    
    def main(self):
        for i in range(self._rows):
            line = []
            for j in range(self._cols):
                line.append(Entry(self.root_f, width=6))
                line[-1].grid(column=j, row=i+1)
                line[-1].insert(0, self._result[i][j])
                line[-1].configure(state='readonly')
            self._map.append(line)
        
        self.start()

from tkinter import *
from functools import partial

from table_edit import GUI as g
from execute_command import GUI as gi
from common.com import Scheme
from table_create import GUI as gu

class GUI(Scheme):
    def __init__(self, db):
        super().__init__('Chose', with_menu=True)
        self.db = db

        self._Add = Menu(self.tools, tearoff=0)
        self._Command = Menu(self.tools, tearoff=0)

        self.list_of_cols = []
        self.cols = []
        self.limit = 3

        self.widgets = []

        self.stop = False

        self.primary()
        self.show_ex()
        self.main()
    
    def primary(self):
        cols = self.db.make_command(f'show tables from {self.db.db};', False)
        if type(cols) == int:
            Label(self.root_w, text='Неверные пользовательские данные!').grid(column=0, row=3)
            return 1
        
        for g in range(len(cols)):

            row = []
            row.append(Button(self.root_w, text=cols[g][0], command=partial(self.go_to_edit, cols[g][0]), width=35))
            self.widgets.append(row[-1])
            row[-1].grid(row=g+2, column=0)
            
            self.cols.append(cols[g][0])
            self.list_of_cols.append(row)
    
    def go_to_edit(self, col):
        g(self.db, col)
    
    def add_new(self):
        gu(self.db)

    def update(self):
        self.clean()
        self.widgets.clear()

        self.primary()

    def clean(self):
        for el in self.widgets:
            el.destroy()
    
    def show_ex(self):
        if not self.stop:

            self.command = Entry(self.root_w, width=35)
            self.accept = Button(self.root_w, text='Выполнить', command=self.execute)
            self.tables_mark = Label(self.root_w, text='Таблицы')
            self.update_b = Button(self.root_w, text="Обновить", command=self.update)

            self.command.grid(column=0, row=0)
            self.accept.grid(column=1, row=0)
            self.tables_mark.grid(column=0, row=1)
            self.update_b.grid(column=1, row=1)
        
            self._Add.add_command(label='Добавить таблицу', command=self.add_new)
            self.tools.add_cascade(label="Добавить", menu=self._Add)

    def execute(self):
        gi(self.db, self.db.db).main(self.command.get(), self)
    
    def main(self):

        self.start()
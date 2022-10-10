from tkinter import *
from table_edit import GUI as g
from execute_command import GUI as gi
from common.com import Scheme
from functools import partial

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

        self.show_ex()
        self.primary()
        self.main()
    
    def primary(self):
        cols = self.db.make_command(f'show tables from {self.db.db};', False)

        if cols == 1:
            lab = Label(self.root_w, text='Bad Request From MySQL: Check User Data')
            lab.grid(column=0, row=0)
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
        pass

    def update(self):
        self.clean()
        self.widgets.clear()

        self.primary()

    def clean(self):
        for el in self.widgets:
            el.destroy()
    
    def show_ex(self):
        self.command = Entry(self.root_w, width=35)
        self.accept = Button(self.root_w, text='Выполнить', command=self.execute)
        self.tables_mark = Label(self.root_w, text='Таблицы')

        self.command.grid(column=0, row=0)
        self.accept.grid(column=1, row=0)
        self.tables_mark.grid(column=0, row=2)
    
        self._Add.add_command(label='Добавить таблицу', command=self.add_new)
        self.tools.add_cascade(label="Добавить", menu=self._Add)

    def execute(self):
        gi(self.db, self.db.db).main(self.command.get(), self)
    
    def main(self):

        self.start()
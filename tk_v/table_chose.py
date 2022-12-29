from tkinter import *
from functools import partial

from table_edit import GUI as g
from execute_command import GUI as gi
from common.com import Scheme

class GUI(Scheme):

    #инициализация
    def __init__(self, db):
        #главное
        super().__init__('Chose', with_menu=True, with_scroll=True)
        self.db = db

        #дополнительное
        self._Add = Menu(self.tools, tearoff=0)
        self._Command = Menu(self.tools, tearoff=0)

        #персональное для этого окна
        self.list_of_cols = []
        self.cols = []
        self.limit = 3

        self.widgets = []

        self.stop = False

        #вызов стоковых методов
        self.primary()
        self.show_ex()
        self.main()
    
    def primary(self):
        cols = self.db.make_command(f'show tables from {self.db.db};', False)
        if type(cols) == int:#проверка на тип конекшна
            Label(self.root_f, text='Неверные пользовательские данные!').grid(column=0, row=3)
            return 1
        
        for g in range(len(cols)):#создание и позиционирование кнопок
            row = []
            row.append(Button(self.root_f, text=cols[g][0], command=partial(self.go_to_edit, cols[g][0]), width=35))
            self.widgets.append(row[-1])
            row[-1].grid(row=g+2, column=0)
            
            self.cols.append(cols[g][0])
            self.list_of_cols.append(row)
        
        self.cnv.update()
        self.__for_bind__()
    
    def go_to_edit(self, col):#открытие окна редактирования
        g(self.db, col)
    
    def add_new(self):#для добавления таблицы ненаделано но очень хочеца
        return 0

    def update(self):#обновление списка таблиц
        self.clean()
        self.widgets.clear()

        self.primary()

    def clean(self):#очистка окна
        for el in self.widgets:
            el.destroy()
    
    def show_ex(self):#создание и позиционирование выполнителя команд
        if not self.stop:

            self.command = Entry(self.root_f, width=35)
            self.accept = Button(self.root_f, text='Выполнить', command=self.execute)
            self.tables_mark = Label(self.root_f, text='Таблицы')
            self.update_b = Button(self.root_f, text="Обновить", command=self.update)

            self.command.grid(column=0, row=0)
            self.accept.grid(column=1, row=0)
            self.tables_mark.grid(column=0, row=1)
            self.update_b.grid(column=1, row=1)
        
            self._Add.add_command(label='Добавить таблицу', command=self.add_new)
            self.tools.add_cascade(label="Добавить", menu=self._Add)

    def execute(self):#выполнить команду
        gi(self.db, self.db.db).main(self.command.get(), self)
    
    def main(self):#старт(опять)

        self.start()
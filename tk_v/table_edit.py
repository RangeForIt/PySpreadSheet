from tkinter import *
from tkinter import messagebox as mb
from os import path

from common.com import Scheme
from table_actions.table_handler import Handler

class GUI(Scheme):#класс интерфейса
    def __init__(self, db, table):#инициализация класса
        super().__init__("SpreadSheet", (750, 500), (250, 250), True, True)
        self.db = db#объект класса базы данных
        self.table = table#имя таблицы
        self.table_handler = Handler(self.db, self.table)#тейбл хендлер

        self._Add = Menu(self.tools, tearoff=0)#меню добавления
        self._Del = Menu(self.tools, tearoff=0)#меню удаления
        self._Form = Menu(self.tools, tearoff=0)#меню формы

        self._types = self.table_handler.col_types#типы колонок
        self._type_lables = []#массив лейблов колонок
        
        #приминение функций
        self.make_menu()
        self.primary()
        self.main()
    
    def make_menu(self):#методы конфигурации тул бара
        self._Form.add_command(label="Сохранить форму", command=self.save)
        self.tools.add_cascade(label='Форма', menu = self._Form)

        #self._Add.add_command(label="Колонку", command=self.insert_col)
        self._Add.add_command(label="Строку", command=self.insert_row)  
        self.tools.add_cascade(label='Добавить', menu=self._Add)

        #self._Del.add_command(label="Колонку", command=self.delete_col)
        self._Del.add_command(label="Строку", command=self.delete_row)  
        self.tools.add_cascade(label='Удалить', menu = self._Del)
    
    def check_pos(self):#инициалмзация позиций ентри
        for i in range(self._rows):
            for j in range(self._cols):
                self._map[i][j].grid(column=j, row=i + 1)

        return 0
    
    def primary(self):#для лейблов
        for i in range(len(self._types)):#выставление лейблов
            self._type_lables.append(Label(self.root_f, text=str(self._types[i][0]).upper()))
        
        for i in range(len(self._type_lables)):#позиционирование лейблов
            self._type_lables[i].grid(column=i, row=0)
            
    def change_color(self, event):#метод смены цвета ентри
        event.widget['bg'] = self.from_rgb((215, 212, 219))
        try:
            event.widget['activebackground'] = self.from_rgb((215, 212, 219))
        except TclError:
            pass

    def insert_col(self):#добавить колонку
        return 0

    def insert_row(self):#добавить строку
        tmp = []

        for i in range(self._cols):
            tmp.append(Entry(self.root_f, width=6))
            tmp[-1].bind('<Button-1>', self.change_color)

        self._rows += 1

        self._map.append(tmp)

        self.check_pos()
        self.__for_bind__()
        return 0


    def delete_row(self):#удалить строку
        if self._rows <= 1:
            mb.showerror('Ошибка', 'Должна быть хотя бы одна строка!')
            return 0

        for i in range(self._cols):
            self._map[-1][i].destroy()

        self._map.pop(-1)
        self._rows -= 1

        self.check_pos()
        self.__for_bind__()
        return 0
    
    def delete_col(self):#удалить колонку
        return 0
    
    def clean(self):#очистить виджеты
        for i in range(self._rows):
            for j in range(self._cols):
                self._map[i][j].destroy()
            self._map.pop(i)
        
        self._rows = 0
        self._cols = 0
    
    def get_data(self):#полуить значения ентри в двумерный массив
        result = []
        for i in range(len(self._map)):#строка
            cols = []
            for j in range(len(self._map[i])):#колонка
                try:
                    cols.append(int(self._map[i][j].get()))
                except ValueError:
                    cols.append(self._map[i][j].get())

            result.append(cols)
        
        return result

    def save(self):#функция сохранения
        cols = self.db.make_command(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{self.table}';", False)
        
        self.table_handler.save(self, self.get_data(), cols)

    def go_to_ref(self, table, db, event):#для перехода по фореигн кей
        GUI(db, table)

    def main(self):#главная функция
        self.table_handler.load(self)#загрузка таблицы

        if self._cols < len(self._type_lables):#проверка кол-ва колонок
            self._cols = len(self._type_lables)

        self.cnv.update()
        self.__for_bind__()

        self.start()#старт(целых четыре)
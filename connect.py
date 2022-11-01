from os import path
from tkinter import *
from pickle import dump, load

from common.dbOperations import DataBase
from table_chose import GUI as g
from common.com import Scheme

class GUI(Scheme):
    def __init__(self):
        super().__init__('Connect', (250, 500), (185, 125), False, False)

        self.primary()
        self.main()
    
    def primary(self):#создание виджетов
        self.save_state = BooleanVar()

        self.host = Entry(self.root_w, width=30)
        self.database = Entry(self.root_w, width=30)
        self.login = Entry(self.root_w, width=30)
        self.psswd = Entry(self.root_w, width=30)
        self.save = Checkbutton(self.root_w, text='Запомнить', variable=self.save_state)
        self.accept = Button(self.root_w, text="Подключиться", command=self.accepting)

        self.pkl_oper()

        self.host.grid(column=0, row=0)
        self.database.grid(column=0, row=1)
        self.login.grid(column=0, row=2)
        self.psswd.grid(column=0, row=3)
        self.save.grid(column=0, row=4)
        self.accept.grid(column=0, row=5)

    def accepting(self):#переход на выбор таблицы
        if self.save_state.get() == True:
            self.data = [self.host.get(), self.login.get(), self.psswd.get(), self.database.get()]
            self.save_usr()

        g(DataBase(self.host.get(), self.login.get(), self.psswd.get(), self.database.get()))
    
    def pkl_oper(self):#сохранение пользователя
        if path.exists('user\\user.pkl'):
            pass
        else:
            self.data = []
            self.save_usr()

        with open('user\\user.pkl', 'rb') as f:
            data = load(f)
            if not data:
                self.host.insert(0, 'Хост')
                self.database.insert(0, 'Имя Базы Данных')
                self.login.insert(0, 'Логин')
                self.psswd.insert(0, 'Пароль')
            
            else:
                self.psswd.configure(show='*')

                self.host.insert(0, data[0])
                self.database.insert(0, data[3])
                self.login.insert(0, data[1])
                self.psswd.insert(0, data[2])

                self.save_state.set(True)
    
    def save_usr(self):
        with open('user\\user.pkl', 'wb') as f:
            dump(self.data, f)
    
    def main(self):
        self.start()

gui = GUI()
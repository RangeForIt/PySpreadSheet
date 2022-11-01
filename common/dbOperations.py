import datetime
import mysql.connector
from mysql.connector import Error
from mysqlx import DatabaseError

class DataBase():#класс базы данных

    def __init__(self, host, user, password, database):
        self.log_file = open('common/logs.log', 'a+')
        self.__log__('Program start here.', add_symb='\n\n')

        self.host_name = host
        self.user_name = user
        self.user_password = password
        self.db = database
        self.connection = self.connect()

        self.__log__(f'User {self.user_name} at host {self.host_name}')

    def connect(self):#метод для подключения
        try:
            connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.user_password,
                database=self.db
            ) 
            self.__log__('Connection is OK.')

            return connection

        except Error as e:
            self.__log__(f'Connection is corruped. Error:\n{e}.')
            return 1

    def make_command(self, command, is_change):#метод для выполнения команл скюл
        try:
            self.cursor = self.connection.cursor()
            self.__log__('Cursor for command is OK.')
        except AttributeError as e:
            self.__log__(f'Cursor for command is corruped. Error:\n{e}')
            return 1

        try:
            if is_change:#если второй аргумент тру, то команда должна что-то добавлять\изменять\удалять, а если фолз, то возвращать штуки
                self.cursor.execute(command)
                self.connection.commit()
                self.__log__(f'Command "{command}" completed with is_change = True.')
                return 'Command Execute Sucsessful!'
            
            else:
                self.cursor.execute(command)
                self.__log__(f'Command "{command}" completed with is_change = False.')
                return self.cursor.fetchall()
                 
        except Error as e:
            self.__log__(f'Command complete is corruped.Error:\n{e}')
            return e
    
    def __log__(self, text, **kwargs):
        if kwargs:
            self.log_file.write(kwargs['add_symb'] + f'DataBase:{datetime.datetime.now()}:{text}\n')
        
        else:
            self.log_file.write(f'DataBase:{datetime.datetime.now()}:{text}\n')
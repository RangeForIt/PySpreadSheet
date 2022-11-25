import mysql.connector
from mysql.connector import Error

from common.logger import Logger

class DataBase():#класс базы данных

    def __init__(self, host, user, password, database):
        self.logger = Logger('DataBase', 'common/logs.log')

        self.host_name = host
        self.user_name = user
        self.user_password = password
        self.db = database
        self.connection = self.connect()

        if type(self.connection) == int:
            self.logger.log(f'Fail login for user {self.user_name} at host {self.host_name}.')
        else:
            self.logger.log(f'Complite login for user {self.user_name} at host {self.host_name}.')
            return

    def connect(self):#метод для подключения
        try:
            connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.user_password,
                database=self.db
            ) 
            self.logger.log('Connection is OK.')

            return connection

        except Error as e:
            self.logger.log(f'Connection is corruped. Error:\n{e}')
            return 1

    def make_command(self, command, is_change):#метод для выполнения команл скюл
        try:
            self.cursor = self.connection.cursor()
            self.logger.log('Cursor for command is OK.')
        except AttributeError as e:
            self.logger.log(f'Cursor for command is corruped. Error:\n{e}')
            return 1

        try:
            if is_change:#если второй аргумент тру, то команда должна что-то добавлять\изменять\удалять, а если фолз, то возвращать штуки
                self.cursor.execute(command)
                self.connection.commit()
                self.logger.log(f"Command '{command}' completed with is_change = True.")
                return 'Command Execute Sucsessful!'
            
            else:
                self.cursor.execute(command)
                self.logger.log(f"Command '{command}' completed with is_change = False.")
                return self.cursor.fetchall()
                 
        except Error as e:
            self.logger.log(f'Command complete is corruped.Error:\n{e}')
            return e
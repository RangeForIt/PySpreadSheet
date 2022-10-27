import mysql.connector
from mysql.connector import Error
import logging

class DataBase():#класс базы данных

    def __init__(self, host, user, password, database):
        self.host_name = host
        self.user_name = user
        self.user_password = password
        self.db = database
        self.connection = self.connect()

        logging.basicConfig(filename=open('logs.log', 'w'), encoding='utf-8', level=logging.INFO)
        logging.info('Program Start')

    def connect(self):#метод для подключения
        try:
            connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.user_password,
                database=self.db
            ) 
            logging.info('Connection is OK.')
            return connection
        except Error as e:
            logging.error(f'Connection is corruped.Error:\n{e}.')
            return 1

    def make_command(self, command, is_change):#метод для выполнения команл скюл
        try:
            cursor = self.connection.cursor()
            logging.info('Cursor is OK.')
        except AttributeError as e:
            logging.error(f'Connection is corruped.Error:\n{e}')
            return 1

        try:
            if is_change:#если второй аргумент тру, то команда должна что-то добавлять\изменять\удалять, а если фолз, то возвращать штуки
                cursor.execute(command)
                self.connection.commit()
                logging.info(f'Command "{command}" completed with is_change = True.')
                return 'Command Execute Sucsessful!'
            
            else:
                cursor.execute(command)
                logging.info(f'Command "{command}" completed with is_change = False.')
                return cursor.fetchall()
                 
        except Error as e:
            logging.error(f'Command complete is corruped.Error:\n{e}')
            return e
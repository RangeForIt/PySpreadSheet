import mysql.connector
from mysql.connector import Error

class DataBase():#класс базы данных

    def __init__(self, host, user, password, database):
        self.host_name = host
        self.user_name = user
        self.user_password = password
        self.db = database
        self.connection = self.connect()

    def connect(self):#метод для подключения
        try:
            connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.user_password,
                database=self.db
            ) 
            return connection
        except Error as e:
            return 1

    def make_command(self, command, is_change):#метод для выполнения команл скюл
        try:
            cursor = self.connection.cursor()
        except AttributeError:
            return 1

        try:
            if is_change:#если второй аргумент тру, то команда должна что-то добавлять\изменять\удалять, а если фолз, то возвращать штуки
                cursor.execute(command)
                self.connection.commit()
                return 'Command Execute Sucsessful!'
            
            else:
                cursor.execute(command)
                return cursor.fetchall()
                 
        except Error as e:
            return e
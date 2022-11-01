from functools import partial
from tkinter import Entry
from mysql.connector import DatabaseError
from idlelib.tooltip import Hovertip
from tkinter import messagebox as mb

class Handler():#класс хендлера таблиц
    def __init__(self, db, table):
        self.db = db
        self.table = table
        self.col_types = self.db.make_command(f'SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = "{self.table}";', False)
    
    def save(self, obj, data, cols_data):#метод сохранения
        is_foreign = False
        foreigns = []
        ct_query = f'create table {self.table}('
        cols_names = []

        for col in cols_data:
            cols_names.append(col[3])
        

        for col in cols_data:#генерация запроса create table
            tmp_ct_query = ''
            tmp_ct_query += col[3] + ' '#+ название

            if col[7] == 'varchar':#есть ли варчары
                tmp_ct_query += f'{col[7]}({col[8]})' + ' '
            else:
                tmp_ct_query += str(col[7]) + ' '
                
            if col[16] == 'PRI':#проверка на примари кей
                tmp_ct_query += 'primary key' + ' '

            elif col[16] == 'MUL':
                foreigns.append(col[3])
                is_foreign = True

            else:
                pass

            if col[17] == 'auto_increment':#проверка на инкремент
                tmp_ct_query += 'auto_increment' + ' '
            else:
                pass
            
            if col != cols_data[-1] or is_foreign:#проверка на конец
                tmp_ct_query += ', '

            ct_query += tmp_ct_query
        
        if is_foreign:
            ct_query += self.create_foreign(self.db.make_command(f'SELECT RC.TABLE_NAME, RC.REFERENCED_TABLE_NAME, KCU.COLUMN_NAME, KCU.REFERENCED_COLUMN_NAME FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS RC JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE KCU USING(CONSTRAINT_NAME) WHERE RC.TABLE_NAME = "{self.table}";', False))
        
        ct_query += ');'
        
        iv_querys = []
        iv_query = f'insert into {self.table}('
        iv_tmp_query = ''
        border = len(cols_names) - 1
        for i in range(len(cols_names)):
            
            if cols_data[i][17] == 'auto_increment':
                continue
            else:
                pass
            if i != border:
                iv_tmp_query += cols_names[i] + ', '
            else:
                iv_tmp_query += cols_names[i]
        
        iv_query += iv_tmp_query

        iv_query += ') values('
        iv_tmp_query = iv_query

        for i in range(len(data)):#генерация insert запроса
            for j in range(len(data[i])):
                flag = False

                if (cols_data[j][7] == 'varchar' or cols_data[j][7] == 'text') and not self.type_check(data[i][j], str):
                    mb.showerror('Ошибка', f'Неверный тип данных!')
                    obj._map[i][j]['bg'] = 'red'
                    obj._map[i][j]['activebackground'] = 'red'
                    flag = True

                if (cols_data[j][7] == 'tinyint' or cols_data[j][7] == 'int') and not self.type_check(data[i][j], int):
                    mb.showerror('Ошибка', f'Неверный тип данных!')
                    obj._map[i][j]['bg'] = 'red'
                    obj._map[i][j]['activebackground'] = 'red'
                    flag = True
                
                if flag:
                    return 1

                border = len(data[i]) - 1
                
                if cols_data[j][7] == 'varchar' or cols_data[j][7] == 'text':

                    if j == border:

                        iv_query += f'"{data[i][j]}"'
                        continue

                    iv_query += f'"{data[i][j]}", '
                    continue
                
                if cols_data[j][16] == 'MUL':
                    pass

                if cols_data[j][17].lower() == 'auto_increment':
                    continue
            
                if j == border:

                    iv_query += str(data[i][j])
                    continue

                iv_query += str(data[i][j]) + ', '
            
            iv_query += ');'
            iv_querys.append(iv_query)
            iv_query = iv_tmp_query
        
        self.override_table(ct_query, iv_querys)

        return 0
            
    def load(self, window):#метод загрузки
        table = self.db.make_command(f'select * from {self.table};', False)
        data = self.db.make_command(f'select * from information_schema.columns where table_name = "{self.table}";', False)
        data_add = self.db.make_command(f'SELECT RC.TABLE_NAME, RC.REFERENCED_TABLE_NAME, KCU.COLUMN_NAME, KCU.REFERENCED_COLUMN_NAME FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS RC JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE KCU USING(CONSTRAINT_NAME) WHERE RC.TABLE_NAME = "{self.table}";', False)

        if not table:
            return 1

        window.clean()

        window._cols = len(table[0])
        window._rows = len(table)

        for i in range(window._rows):
            line = []
            for j in range(window._cols): 
                line.append(Entry(window.root_f, width=6))
                line[-1].bind('<Button-1>', window.change_color)
                if data[j][16] == 'MUL':
                    line[-1].bind('<Button-3>', partial(window.go_to_ref, data_add[j - 1][1], self.db))
                    Hovertip(line[-1], 'Нажмите ПКМ')

                line[-1].insert(0, table[i][j])
            window._map.append(line)

        window.check_pos()

        return 0
    
    def type_check(self, object, necessary_type):
        if type(object) != necessary_type:
            return False
        
        else:
            pass

        return True

    def override_table(self, ct_query, iv_querys):#метод перезаписи таблицы
        self.test_for_error(self.db.make_command(f"drop table {self.table};", True))
        #print(ct_query, iv_querys)

        if self.test_for_error(self.db.make_command(ct_query, True)):
            return 1
        for el in iv_querys:
            if self.test_for_error(self.db.make_command(el, True)) == 1:
                return 1
            
            else:
                pass
        
        mb.showinfo("Успешно", "Таблица успешно сохранена!")
        return 0
    
    def test_for_error(self, exp):
        if DatabaseError in type(exp).__bases__:
            mb.showerror('Ошибка', f'Произошла ошибка!\n{exp}')
            return 1
    
        else:
            return 0 
    
    def create_foreign(self, data):
        #print(data)
        result_tmp = 'foreign key ('
        result = result_tmp
        for i in range(len(data)):
            for el in data:
                if el[1] == data[i][1]:
                    try:
                        if data[i + 1][1] == el[1]:
                            result += el[2] + ', '
                        
                        else:
                            result += el[2]
                            break
                    
                    except IndexError:
                        result += el[2]
                        break
                else:
                    continue

            result += f') references {data[i][1]} ('
            for el in data:
                if el[1] == data[i][1]:
                    try:
                        if data[i + 1][1] == el[1]:
                            result += el[3] + ', '
                        
                        else:
                            result += el[3]
                            break
                    
                    except IndexError:
                        result += el[3]
                        break
                else:
                    continue
            
            if data[i] != data[-1]:
                result += '), '
                result += result_tmp
            
            else:
                result += ')'
        
        return result
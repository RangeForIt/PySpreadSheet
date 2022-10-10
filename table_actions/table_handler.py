from tkinter import Entry
from tkinter import messagebox as mb

class Handler():#класс хендлера таблиц
    def __init__(self, db, table):
        self.db = db
        self.table = table
        self.col_types = self.db.make_command(f'SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = "{self.table}";', False)
    
    def save(self, obj, data, cols_data):#метод сохранения
        ct_query = f'create table {self.table}('
        cols_names = []

        for i in range(len(cols_data)):
            cols_names.append(cols_data[i][3])
        
        border = len(cols_data) - 1
        for i in range(len(cols_data)):#генерация запроса create table
            if cols_data[i][7] == 'varchar':
                if i == border:
                    ct_query += f'{cols_data[i][3]} {cols_data[i][7]}({cols_data[i][8]}) {cols_data[i][16]} {cols_data[i][17]}'
                    continue

                ct_query += f'{cols_data[i][3]} {cols_data[i][7]}({cols_data[i][8]}) {cols_data[i][16]} {cols_data[i][17]},'
                continue

            if i == border:
                ct_query += f'{cols_data[i][3]} {cols_data[i][7]} {cols_data[i][16]} {cols_data[i][17]}'
                continue
            
            if cols_data[i][16].lower() == 'pri':
                if i == border:
                    ct_query += f'{cols_data[i][3]} {cols_data[i][7]}({cols_data[i][8]}) {cols_data[i][16]} {cols_data[i][17]}'
                    continue
                ct_query += f'{cols_data[i][3]} {cols_data[i][7]} primary key {cols_data[i][17]},'
                continue

            ct_query += f'{cols_data[i][3]} {cols_data[i][7]} {cols_data[i][16]} {cols_data[i][17]},'
        
        ct_query += ');'
        
        iv_querys = []
        iv_query = f'insert into {self.table}('
        border = len(cols_names) - 1
        for i in range(len(cols_names)):
            if i == border:
                iv_query += cols_names[i]
                continue

            if cols_data[i][17].lower() == 'auto_increment':
                continue
            
            iv_query += cols_names[i] + ', '

        iv_query += ') values('
        iv_tmp_query = iv_query

        for i in range(len(data)):#генерация insert запроса
            for j in range(len(data[i])):
                flag = False

                if (cols_data[j][7] == 'varchar' or cols_data[j][7] == 'text') and not self.type_check(data[i][j], str):
                    print(data[i][j])
                    mb.showerror('Ошибка', f'Неверный тип данных!')
                    obj._map[i][j]['bg'] = 'red'
                    obj._map[i][j]['activebackground'] = 'red'
                    flag = True

                if (cols_data[j][7] == 'tinyint' or cols_data[j][7] == 'int') and not self.type_check(data[i][j], int):
                    print(data[i][j])
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
                
                if cols_data[j][16].lower() == 'pri' and cols_data[j][17].lower() == 'auto_increment':
                    continue

                else:
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

        if not table:
            return 1

        window.clean()

        window._cols = len(table[0])
        window._rows = len(table)

        for i in range(window._rows):
            line = []
            for j in range(window._cols):
                line.append(Entry(window.root_f, width=6))
                line[len(line) - 1].bind('<Button-1>', window.change_color)
                line[len(line) - 1].insert(0, table[i][j])
                line[len(line) - 1].grid(column=j, row=i + 2)
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
        self.db.make_command(f"drop table {self.table};", True)

        self.db.make_command(ct_query, True)
        for el in iv_querys:
            self.db.make_command(el, True)
        
        mb.showinfo("Успешно", "Таблица успешно сохранена!")
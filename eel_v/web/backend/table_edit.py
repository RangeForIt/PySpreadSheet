from web.backend.local.table_handler import Handler
from web.backend.local.error import QueryError

import eel

class Editor:#класс интерфейса
    def __init__(fles, db, table):#инициализация класса
        Editor.db = db
        Editor.table = table
        Editor.handler = Handler(Editor.db, Editor.table)
    
    @eel.expose
    def set_table():
        eel.show_t(Editor.handler.get(), Editor.handler.cols_data)
    
    @eel.expose
    def save(table_d):
        try:
            Editor.handler.save(table_d)
            eel.alerti("Успешно сохранено!")
        except QueryError as e:
            eel.handle_exception(e.err_index)
        
        
    @eel.expose
    def new_r():
        eel.new_row(len(Editor.handler.cols_data))
from tkinter import *
from common_funcs import Funcs

funcs = Funcs()

class GUI:
    def __init__(self, db):
        self._root = Tk()
        self.db = db

        self._root.minsize(250, 250)
        self._root.maxsize(250, 250)

        self.cbb = []

        self.primary()
        self.main()
    
    def primary(self):
        self.name = Entry(self._root)
        
    
    def main(self):
        pass
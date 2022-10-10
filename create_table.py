from tkinter import *
from common.com import Scheme

class GUI(Scheme):
    def __init__(self, db):
        super().__init__('Table Master', (800, 800), (400, 400), False, True)

        self.primary()
        self.main()
    
    def primary(self):
        pass
    
    def main(self):
        pass
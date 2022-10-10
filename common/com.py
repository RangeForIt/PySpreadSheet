from threading import Thread
from tkinter import *
    
class Scheme:
    def __init__(self, title="Window", maxs=(500, 500), mins=(250, 250), with_menu=False, with_scroll=False):
        self.root_w = Tk()

        self.root_w.title(title)
        self.root_w.minsize(mins[0], mins[1])
        self.root_w.maxsize(maxs[0], maxs[1])

        self.__checkargs__(with_menu,  with_scroll)
        
        self._cols = 0
        self._rows = 0

        self._map = []

        self.quit = False
    
    def __for_bind__(self, ev):
        self.cnv.configure(scrollregion=self.cnv.bbox('all'))
    
    def __checkargs__(self, with_menu, with_scroll):
        if with_menu:
            self.tools = Menu(self.root_w)
            self.root_w.configure(menu = self.tools)
        
        if with_scroll:  
            self.cnv = Canvas(self.root_w)
            self.scrollbar = Scrollbar(self.root_w, command=self.cnv.yview)

            self.cnv.configure(yscrollcommand=self.scrollbar.set)
            #self.cnv.bind('<Configure>', self.__for_bind__)

            self.root_f = Frame(self.cnv)

            self.cnv.create_window((0, 0), window=self.root_f, anchor='n')

            self.cnv.grid(column=0, row=0, sticky=N+S)
            self.scrollbar.grid(column=1, row=0, sticky=N+S)
    
    def __startgui__(self):
        while self.quit != True:
            self.root_w.update()
    
    def primary(self):
        pass
    
    def update_scrollbar(self):
        pass
    
    def start(self):
        self.__startgui__()
    
    def from_rgb(self, rgb):
        return "#%02x%02x%02x" % rgb

    def main(self):
        pass
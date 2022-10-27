from tkinter import *
    
class Scheme:#родительский класс
    def __init__(self, title="Window", maxs=(500, 500), mins=(250, 250), with_menu=False, with_scroll=False):#аргументы-параметры окна
        self.root_w = Tk()#создание и конфигурация окна

        self.root_w.title(title)
        self.root_w.minsize(mins[0], mins[1])
        self.root_w.maxsize(maxs[0], maxs[1])

        self.__checkargs__(with_menu,  with_scroll)
        
        self._cols = 0
        self._rows = 0

        self._map = []
    
    def __for_bind__(self):
        self.cnv.configure(scrollregion=self.cnv.bbox('all'))#для скроллбара
    
    def __checkargs__(self, with_menu, with_scroll):#проверка аргументов на тру и фолз
        if with_menu:
            self.tools = Menu(self.root_w)
            self.root_w.configure(menu = self.tools)
        
        if with_scroll:  
            self.cnv = Canvas(self.root_w)
            self.scrollbar = Scrollbar(self.root_w, command=self.cnv.yview)
             
            self.__for_bind__()
            self.cnv.configure(yscrollcommand=self.scrollbar.set)

            self.root_f = Frame(self.cnv)

            self.cnv.create_window((0, 0), window=self.root_f, anchor='nw')

            self.cnv.grid(column=0, row=0, sticky=N+S+W)
            self.scrollbar.grid(column=1, row=0, sticky=N+S+W)
    
    def primary(self):#не для инита, но нужно
        pass
    
    def start(self):#еще старт
        self.root_w.mainloop()
    
    def from_rgb(self, rgb):#для цветов
        return "#%02x%02x%02x" % rgb

    def main(self):#мейн
        pass
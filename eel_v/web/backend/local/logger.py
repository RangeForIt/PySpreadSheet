from datetime import datetime

class Logger:
    def __init__(self, name, path_to_log):
        self.name = name
        self.log_file = open(path_to_log, 'a')
        self.log('Program Start Here', add_symb = '\n\n')
    
    def log(self, text, **kwargs):
        if kwargs:
            self.log_file.write(kwargs['add_symb'] + f'{self.name}:{datetime.now()}:{text}\n')
        
        else:
            self.log_file.write(f'{self.name}:{datetime.now()}:{text}\n')
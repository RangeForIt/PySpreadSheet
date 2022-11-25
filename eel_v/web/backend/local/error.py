class QueryError(Exception):
    def __init__(self, value, err_index):
        self.val = value
        self.err_index = err_index
        self.text = 'Error in query ' + value
    
    def __hash__(self):
        return self.text
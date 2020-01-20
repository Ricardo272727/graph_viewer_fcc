
class Graph_viewer:
    """ 
    The model of application
    """
    def __init__(self):
        # list of open files in the program
        self.files = []
        # index of current file on list
        self.index_current_file = 0

    # this function change the current file in the app
    def current_file(self, index):
        self.index_current_file = index
        
    
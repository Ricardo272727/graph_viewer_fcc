from tkinter import *
import dnd
from config import Config
class View:
    """ 
    This is a class that create a new instance of the graph viewer
    """
    def __init__(self, controller):

        self.f = Config()
        
        self.window = Tk()
        self.c = controller

        # configuration window
        self.window.title("Graph viewer 3000")
        self.window.geometry("900x600")
        self.window.config(bg='#2591f7')

        self.create_menu_bar()
        
        self.create_left_pane()

    def init(self):

        self.window.mainloop()

    def create_left_pane(self):
        self.left_pane = PanedWindow(self.window, bg=self.f.colors['primary'])


    def create_menu_bar(self):
        # menu bar
        self.menu = Menu(self.window)

        # > file
        file_item = Menu(self.window, tearoff=0)
        file_item.add_command(label="New", command=self.c.new_file)
        file_item.add_separator()
        file_item.add_command(label="Open", command=self.c.open_file)
        file_item.add_separator()
        file_item.add_command(label="Open directory", command=self.c.open_directory)
        self.menu.add_cascade(label="File", menu=file_item)
        # > edit
        self.menu.add_cascade(label="Edit", menu=file_item)

        # > view
        self.menu.add_command(label="View")

        # > preferences
        self.menu.add_command(label="Preferences")

        # > about
        self.menu.add_command(label="About")

        self.window.config(menu=self.menu)


    
    def show_graph(self, graph):
        """ Show a graph juasjuas"""
        matrix = graph['adj_matrix']
        vertex = graph['vertex']
        print(matrix)
        print(vertex)


        

        

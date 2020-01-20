from tkinter import filedialog
import graph_viewer
import view

class Controller:
    def __init__(self):
        self.model = None
        self.view = None
        
    def init(self):
        self.view.init()

    def new_file(self):
        """ Show a new widget to create a new file """
        print("Show a new widget to create a new file")
        # open a menu to create a file
        file = filedialog.asksaveasfile(initialdir="~", title="New file", filetypes=(("fcc file","*.fcc"),("grph file","*.grph"), ("gph file", "*.ghp")))
        # if the user create a new file ...
        if file != None:
            # add file to the list of files in app
            self.model.files.append(file)
            # set current file as this
            self.model.current_file(self.model.files.index(file))
            print("Current file: " + file.name)
        
    

    def open_file(self):
        """ Show a new widget to open a file.fcc """
        print("Show a new widget to open a file.fcc ")

        file = filedialog.askopenfilename(filetypes = (
            ("Graph files","*.fcc"), ("Json files", "*.json"), ("All files", "*.*")),
            title="Select file")

        if file != None:
            self.model.files.append(file)
            self.model.current_file(self.model.files.index(file))




    def open_directory(self):
        """ Show a new widget to open a directory """
        print("Show a new widget to open a directory ")
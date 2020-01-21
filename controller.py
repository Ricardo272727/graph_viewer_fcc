from tkinter import filedialog
import graph_viewer
import view
import json
class Controller:
    def __init__(self):
        self.model = None
        self.view = None
        self.filetypes = (("Simple graph file", "*.ghp"), ("Json files", "*.json"))
        """
        lets make peace and not war
        """
    def init(self):
        
        try:
            with open("example_file.json", 'r') as f_obj:
                graph = json.load(f_obj)
                self.view.show_graph(graph)
        except FileNotFoundError:
            print("File not found ")
        self.view.init()
        
    def new_file(self):
        """ Show a new widget to create a new file """
        print("Show a new widget to create a new file")
        # open a menu to create a file
        file = filedialog.asksaveasfile(initialdir="~", title="New file", filetypes=self.filetypes)
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

        file = filedialog.askopenfilename(initialdir="~", filetypes = (self.filetypes), title="Select file")
        print(file)
        if file != None:
            self.model.files.append(file)
            self.model.current_file(self.model.files.index(file))
            self.view.show_file(self.model.files[self.model.index_current_file])
            print("Current file: " + file.name)



    def open_directory(self):
        """ Show a new widget to open a directory """
        print("Show a new widget to open a directory ")
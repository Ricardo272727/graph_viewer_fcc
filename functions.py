from tkinter import filedialog


""" Functions of graphic interface """

def new_file():
    """ Show a new widget to create a new file """
    print("Show a new widget to create a new file")
    
   

def open_file():
    """ Show a new widget to open a file.fcc """
    print("Show a new widget to open a file.fcc ")

    file = filedialog.askopenfilename(filetypes = (
        ("Graph files","*.fcc"), ("Json files", "*.json"), ("All files", "*.*")),
        title="Select file")

def open_directory():
    """ Show a new widget to open a directory """
    print("Show a new widget to open a directory ")
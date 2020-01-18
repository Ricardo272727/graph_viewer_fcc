from tkinter import *
import functions as f
from graph_viewer import Graph_viewer as app

window = Tk()
# configuration window
window.title("Graph viewer 3000")
window.geometry("900x600")
window.config(bg='#2591f7')

# menu bar
menu = Menu(window)

# > file
file_item = Menu(window, tearoff=0)
file_item.add_command(label="New", command=f.new_file)
file_item.add_separator()
file_item.add_command(label="Open", command=f.open_file)
file_item.add_separator()
file_item.add_command(label="Open directory", command=f.open_directory)

menu.add_cascade(label="File", menu=file_item)

# > edit
menu.add_cascade(label="Edit", menu=file_item)

# > view
menu.add_command(label="View")

# > preferences
menu.add_command(label="Preferences")

# > about
menu.add_command(label="About")


window.config(menu=menu)

window.mainloop()

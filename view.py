from tkinter import *
import dnd
from config import Config
class View:
    """ 
    This is a class that create a new instance of the graph viewer
    """
    def __init__(self, controller = None):

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
        #file_item.add_command(label="New", command=self.c.new_file)
        file_item.add_separator()
        #file_item.add_command(label="Open", command=self.c.open_file)
        file_item.add_separator()
        #file_item.add_command(label="Open directory", command=self.c.open_directory)
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
        """ Show a graph juasjuas
        Super objetivos:
        Mostrar un nodo arrastrable
        """
        

class Node:
    def __init__(self, name):
        self.name = name
        self.canvas = self.label = self.id = None

    def attach(self, canvas, x=10, y=10):
        if canvas is self.canvas:
            self.canvas.coords(self.id, x, y)
            return
        if self.canvas:
            self.detach()
        if not canvas:
            return
        label = Label(canvas, text=self.name,
                              borderwidth=2, relief="raised")
        id = canvas.create_window(x, y, window=label, anchor="nw")
        #canvas.create_oval(x, y, 100, 100, fill="#008080", outline="red", width=2)
        
        self.canvas = canvas
        self.label = label
        self.id = id
        label.bind("<ButtonPress>", self.press)

    def detach(self):
        canvas = self.canvas
        if not canvas:
            return
        id = self.id
        label = self.label
        self.canvas = self.label = self.id = None
        canvas.delete(id)
        label.destroy()

    def press(self, event):
        if dnd.dnd_start(self, event):
            # where the pointer is relative to the label widget:
            self.x_off = event.x
            self.y_off = event.y
            # where the widget is relative to the canvas:
            self.x_orig, self.y_orig = self.canvas.coords(self.id)

    def move(self, event):
        x, y = self.where(self.canvas, event)
        self.canvas.coords(self.id, x, y)

    def putback(self):
        self.canvas.coords(self.id, self.x_orig, self.y_orig)

    def where(self, canvas, event):
        # where the corner of the canvas is relative to the screen:
        x_org = canvas.winfo_rootx()
        y_org = canvas.winfo_rooty()
        # where the pointer is relative to the canvas widget:
        x = event.x_root - x_org
        y = event.y_root - y_org
        # compensate for initial pointer offset
        return x - self.x_off, y - self.y_off

    def dnd_end(self, target, event):
        pass
        

class PaneDragDrop:
    def __init__(self, root, width, height):
        self.canvas = Canvas(root, width=width, height=height)
        self.canvas.pack(fill="both", expand=1)
        self.canvas.dnd_accept = self.dnd_accept

    def dnd_accept(self, source, event):
        return self
    
    def dnd_enter(self, source, event):
        self.canvas.focus_set() # show highlight border (no se si se vea bien)
        x, y = source.where(self.canvas, event)
        x1, y1, x2, y2 = source.canvas.bbox(source.id)
        dx, dy, = x2-x1, y2-y1
        self.dndid = self.canvas.create_rectangle(x, y, x+dx, y+dy)
        
        self.dnd_motion(source, event)
    
    def dnd_motion(self, source, event):
        x, y = source.where(self.canvas, event)
        x1, y1, x2, y2 = self.canvas.bbox(self.dndid)
        self.canvas.move(self.dndid, x-x1, y-y1)

    def dnd_leave(self, source, event):
        self.canvas.delete(self.dndid)
        self.dndid = None
    
    def dnd_commit(self, source, event):
        self.dnd_leave(source, event)
        x, y = source.where(self.canvas, event)
        source.attach(self.canvas, x, y)

def test():
    view = View()
    
    node = Node("nodo chido")
    pane = PaneDragDrop(view.window, 200, 200)
    node.attach(pane.canvas)

    view.init()

if __name__ == "__main__":
    test()

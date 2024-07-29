
import tkinter as tk
from .selector import FileSelector
from .graphtk import TkGraph

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.graph = TkGraph(self)
        self.graph.place(relx=0, rely=0, relwidth=1, relheight=0.9)
        self.selector = FileSelector(self, text="Logfile")
        self.selector.place(relx=0, rely=0.9, relwidth=1, relheight=0.05)
        self.generate_button = tk.Button(self, text="Generate Graph", bg="light green")
        self.generate_button.place(relx=0, rely=0.95, relwidth=1, relheight=0.05)
        self.geometry("800x800")
        self.protocol("WM_DELETE_WINDOW", lambda: self.quit() or self.destroy())

    def set_generate_button_command(self, command):
        self.generate_button.config(command=command)
    
    def append(self, line_name, date, y):
        self.graph.append(line_name, date, y)
    
    def draw(self):
        self.graph.show()
        
    def clear(self):    
        self.graph.clear()

    def get_path(self):
        return self.selector.get_path()
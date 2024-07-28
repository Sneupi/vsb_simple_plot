import tkinter as tk
from tkinter import filedialog

class FileSelector(tk.Frame):
    """Generic file browser Frame for selecting a 
    file and performing a specific action on it."""
    def __init__(self, master, text="[Filename]", toggle_func=None):
        super().__init__(master)
        super().configure(width=600, height=50)
        self.browse_button = tk.Button(self, text=f"Select {text}", command=self.select_file)
        self.browse_button.place(relx=0, rely=0, relwidth=0.2, relheight=1)
        
        self.label = tk.Label(self, text="File:")
        self.label.place(relx=0.2, rely=0, relwidth=0.1, relheight=1)
        
        self.filepath_label = tk.Label(self, borderwidth=2, relief="groove")
        self.filepath_label.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        
    def select_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.filepath_label.config(text=path)
            
    def get_path(self):
        return str(self.filepath_label.cget("text"))

from .graph import Graph
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
import datetime

class TkGraph(tk.Frame):
    """Generic tkinter.Frame LiveGraph using graph.LiveGraph.
    
    NOTE: Enforces datetime units of width."""
        
    def append(self, line_name, date, val):
        self.graph.append(line_name, date, val)
    
    def show(self):
        self.graph.draw()
        
    def clear(self):
        self.graph.clear()
    
    def __init__(self, master):
        super().__init__(master)
        
        def manual_scroll(event):
            self.graph.set_xlim_to_relx(self.scroll_slider.get()/100)
            
        def update_width(event=None):
            time_units = {
                "Seconds": 1,
                "Minutes": 60,
                "Hours": 3600,
                "Days": 86400
            }
            unit = self.unit_var.get()
            width = self.width_slider.get() * time_units[unit]
            self.graph.set_width(datetime.timedelta(seconds=width))
        default_seconds = 10
        self.graph = Graph(width=datetime.timedelta(seconds=default_seconds))
        self.canvas = FigureCanvasTkAgg(self.graph.fig, master=self)
        self.canvas.get_tk_widget().place(relx=0, rely=0, relwidth=1, relheight=0.85)
        
        self.scroll_slider = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        self.scroll_slider.set(100)
        self.scroll_slider.bind("<B1-Motion>", manual_scroll)
        self.scroll_slider.place(relx=0, rely=0.9, relwidth=1, relheight=0.05)
        
        time_units = ["Seconds", "Minutes", "Hours", "Days"]
        self.unit_var = tk.StringVar(self)
        self.unit_var.set(time_units[0])
        self.unit_menu = tk.OptionMenu(self, self.unit_var, *time_units)
        self.unit_menu.place(relx=0, rely=0.95, relwidth=0.1, relheight=0.05)
        
        self.unit_updater_button = tk.Button(self, text="Update Units", 
                                             command=update_width)
        self.unit_updater_button.place(relx=0.1, rely=0.95, relwidth=0.1, relheight=0.05)
        
        self.width_slider = tk.Scale(self, from_=1, to=100, orient=tk.HORIZONTAL)
        self.width_slider.bind("<B1-Motion>", update_width)
        self.width_slider.set(default_seconds)
        self.width_slider.place(relx=0.2, rely=0.95, relwidth=0.8, relheight=0.05)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.place(relx=0, rely=0.85, relwidth=1, relheight=0.05)
        

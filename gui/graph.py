
from .helpers import LinesHandler, LimitHandler
import matplotlib.pyplot as plt

class Graph:
    """Live matplotlib graph with interactive interface."""
    def __init__(self, width, enable_pick_event=True):
        """NOTE: units/type of x must be consistent for all provided values.
        
        Args:
            width (Any): Width of the graph in x-axis units
            interval (int): Refresh interval millis.
        """
        self.fig, self.ax = plt.subplots()
        self.ax.grid()
        self.ax.tick_params(axis='x', rotation=45)
        self.fig.subplots_adjust(bottom=0.11, top=0.99, left=0.06, right=0.99)
        
        self.lines = LinesHandler(self.ax, self.fig, enable_pick_event)
        self.limits = LimitHandler(self.ax, width)
        
    def append(self, line_name, x, y):
        """Append data to the graph at line"""
        self.limits.track_data(x, y)
        self.lines.append(line_name, x, y)
        
    def set_width(self, width):
        """Set the width of the graph in x-axis units."""
        self.limits.set_width(width)
        self.fig.canvas.draw_idle()
    
    def set_xlim_to_relx(self, percent: float):
        """View graph at relative x between 0.0 (xmin) and 1.0 (xmax)."""
        self.limits.set_xlim_to_relx(percent)
        self.fig.canvas.draw_idle()
        
    def clear(self):
        """Clear all lines from graph"""
        self.lines.clear_all()
        self.limits.clear_tracked()
        self.fig.canvas.draw_idle()
    
    def draw(self):
        self.limits.set_xlim_to_autoscale()
        self.limits.set_ylim()
        self.fig.canvas.draw_idle()
    
    def show(self):
        """Show the graph if it is not 
        handled by any other mainloop (e.g. tkinter)"""
        plt.show()

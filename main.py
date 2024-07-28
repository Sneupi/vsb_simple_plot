"""
Graph that populates itself from a properly
formatted CSV containing cell voltage array data

Rows are formatted as regex: 
\d+-\d+-\d+ \d+:\d+:\d+.\d+,.*,.*DBG CV.\d+:\s+\d+*

With timestamp formatted as: 
%Y-%m-%d %H:%M:%S.%f
"""
from gui.gui import GUI

import verify
import re
import datetime

def generate_graph(gui: GUI):
    path = gui.get_path()
    try:
        verify.log_path(path)
    except Exception as e:
        print(f"\033[91m[FILE]\033[0m {e}")
        return
    
    print("Generating graph...")
    gui.clear()
    with open(path, 'r') as file:
        for line in file:
            if re.search(r'.*DBG CV.*', line):
                print("Adding line:" + line.strip())
                date_format = "%Y-%m-%d %H:%M:%S.%f"
                date_string = line.split(',')[0]
                date = datetime.datetime.strptime(date_string, date_format)
                ch, val = re.findall(r'\d+', line)[-2:]
                gui.append(ch, date, int(val)) 
    gui.draw()
    
gui = GUI()
gui.set_generate_button_command(lambda: generate_graph(gui))
gui.mainloop()

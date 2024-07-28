"""
Verify input variables required to start the program.
"""
import os
    
def log_path(log_path: str):
    """passes no errors if log path ok"""
    if not os.path.exists(log_path):
        raise FileNotFoundError(f'Log file does not exist: {log_path}')
    elif not log_path.endswith(('.csv', '.txt')):
        raise ValueError(f'Log file must end in .csv or .txt: {log_path}')
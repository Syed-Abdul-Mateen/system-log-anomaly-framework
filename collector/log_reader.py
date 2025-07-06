# collector/log_reader.py

import os

def read_log_file(filepath):
    """
    Reads a static log file (.log, .txt, .json) and returns a list of lines.
    
    Args:
        filepath (str): Full path to the log file
    
    Returns:
        list: Lines of the log file
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Log file not found: {filepath}")

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
    
    return [line.strip() for line in lines if line.strip()]

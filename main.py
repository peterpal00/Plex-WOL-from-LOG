from pygtail import Pygtail
from time import sleep
import os

def main():
    
    log_file_path = '/logfile'
    log_file_path_part = os.environ['LOG_FILE_PATH_PART']
    log_file_name = os.environ['LOG_FILE_NAME']
    
    # Get the path to the log file
    log_file = os.path.join(log_file_path, log_file_path_part, log_file_name)
    
    while(True):
        for line in Pygtail(log_file, offset_file = 'offset_file.offset'):
            print(line)
        sleep(2)
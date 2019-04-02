from datetime import date, datetime
import time
import os

def Output_Path_Set():
    now = datetime.now()
    path_current_time = now.strftime("%H-%M-%S__%d-%b-%Y")

    try:
        os.makedirs(path_current_time)
        os.chdir(path_current_time)    
    except FileExistsError:
        print(path_current_time,"FIle already exists")

    return path_current_time
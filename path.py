from datetime import date
import time
import os
now=time.ctime()
today = str(date.today())
print(today)
try:
    os.makedirs("Output")    
    print("Directory " , "Output" ,  " Created ")
except FileExistsError:
    print("Output","FIle already exists")
print(now)
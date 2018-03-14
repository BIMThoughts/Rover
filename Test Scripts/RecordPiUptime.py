# This is a simple python script that will record the date and time every 120 seconds
# I used this script to record the current time and date during my battery tests
import time
from datetime import datetime
while True:
    f = open('uptime.txt','a')
    f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    f.write('\n')
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    f.close()
    time.sleep (120)
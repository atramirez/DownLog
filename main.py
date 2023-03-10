"""
author: atramirez

description: Main file to check internet is out and log
"""

import subprocess
import time
import datetime
import csv

def ping_google():
    """
    returns: True if google can be reached
    """
    return subprocess.call(['ping', '-c', '1', 'google.com'])

def add_entry(time, internet_down):
    with open("down_log.csv", "w") as log_file:
        writer = csv.writer(log_file)
        writer.writerow([time, internet_down])

def main():
    internet_down = False
    with open("down_log.csv", "w") as log_file:
        writer = csv.writer(log_file)
        writer.writerow(['Timestamp', 'Status'])
        
    add_entry(cur_time, ping_google())

    while(True):
        time.sleep(60)
        cur_time = datetime.datetime.now()
        cur_status = ping_google() 
        if cur_status != 0 and not internet_down: # If bad return and internet is currently up
            add_entry(cur_time, True)
        elif cur_status == 0 and internet_down: # If good return and internet is currently down
            add_entry(cur_time, False)

if __name__ == "__main__":
    main()

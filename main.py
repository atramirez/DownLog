"""
author: atramirez

description: Main file to check internet is out and log
"""

import subprocess
import time
import datetime
import csv

def ping_google():
    return subprocess.check_output(['ping', '-c', '1', 'google.com'])

def get_internet_up_status():
    try:
        ping_google()
        up_status = True 
    except subprocess.CalledProcessError:
        up_status = False
    return up_status

def add_entry(time, internet_down, file):
    with open(file, "a") as log_file:
        writer = csv.writer(log_file)
        writer.writerow([time, internet_down])
        log_file.close()

def main():
    internet_down = False
    file_name = f"downlog-{datetime.datetime.now()}.csv"
    with open(file_name, "w") as log_file:
        writer = csv.writer(log_file)
        writer.writerow(['Timestamp', 'Status(Up=1)'])
        log_file.close()

    print("Startup: Initial Ping")
    print("----------------------------------------------------")   
    add_entry(datetime.datetime.now(), get_internet_up_status(), file_name)

    while(True):
        time.sleep(60)
        print("doing it ")
        cur_time = datetime.datetime.now()
        up_status = get_internet_up_status()
        
        if up_status == False and not internet_down: # If bad return and internet is currently up
            add_entry(cur_time, False, file_name)
            internet_down = True
            print(f"{cur_time}:** Updating Internet Status to Down **")
            print("----------------------------------------------------") 
        elif up_status == True and internet_down: # If good return and internet is currently down
            add_entry(cur_time, True, file_name)
            internet_down = False
            print(f"{cur_time}:** Updating Internet Status to Up **")
            print("----------------------------------------------------") 


if __name__ == "__main__":
    main()

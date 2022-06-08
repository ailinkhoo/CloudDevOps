# Python program to explain os.system() method 
# #python script that runs git commands on a specified schedule.
	
# importing module
import os
import schedule
import time
from datetime import datetime

# Command to execute
# Using Windows OS command

cmd = 'git add . && git commit -m "Update every tuesday" && git push'


# Using os.system() method
# Functions setup

def update_github():
	os.system(cmd)
	print(datetime.now())

# Task scheduling: https://www.geeksforgeeks.org/python-schedule-library/

# Every Tuesday at 20:00 update_github() is called

schedule.every().tuesday.at("20:00").do(update_github)

# for testing: schedule.every(1).minutes.do(update_github)

# Loop so that the scheduling task
# keeps on running all time.
while True:

	# Checks whether a scheduled task
	# is pending to run or not
	schedule.run_pending()
	time.sleep(1)

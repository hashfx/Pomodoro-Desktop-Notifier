"""
Pomodoro desktop notification program
    pomodoro technique: work for 25 minutes; take a break of 5 minutes
"""

# import required modules

# pip install plyer
from plyer import notification
import time

while True:
    notification.notify(
        title='Take a Break', # title of notification window
        message='Take a break, Champion!', # message to be displayed in notification
        app_icon='icon.ico', # path of icon of notifier // dont forget to include icon in project dir
        timeout=10, # stay-duration(in sec) of notification on screen
    )
    time.sleep(60*60) # display notification every hour

'''
To run the script every hour:
open terminal
    type: pythonw .\Notifier.py
'''

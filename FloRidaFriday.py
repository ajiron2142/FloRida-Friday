import webbrowser
import keyboard
import time as time_module 
import pyautogui
import subprocess
import math
from datetime import datetime, time 
#import tkinter   look into this


todays_date = datetime.today()
day_of_week_string = todays_date.strftime('%A')
day_of_week_integer = todays_date.weekday()
volume_level = 9 #math.ceil((day_of_week_integer + 1) * 14.28) 
current_time = datetime.now().time()
eight_am = time(8, 0, 0)
print(f"Today is {day_of_week_string}. The volume will be set to {volume_level}.")

def set_volume():
    subprocess.run(['osascript', "-e", f'set volume output volume {volume_level}'])


url0 = 'https://music.youtube.com/watch?v=Q_mQxKviRJM'
url1 = 'https://music.youtube.com/watch?v=WJM7DNwxypA&si=Hdnf7rfAPMki_Mp1'
url2 = 'https://music.youtube.com/watch?v=uUL8a7eJCk8&si=bLD-lqiYqZyVpHx3'
url3 = 'https://music.youtube.com/watch?v=6Y24X4oTQLA&si=aJXLpyUDudnYWVyP'
url4 = 'https://music.youtube.com/watch?v=88gZ5bw7GU4&si=lrsvHioYm1izm51k'
url5 = 'https://music.youtube.com/watch?v=c2S1x2kTYJM&si=KyGXRDxgKUWyzbPQ'
url6 = 'https://music.youtube.com/watch?v=mTdC0al9fII&si=N7CABCHn97xluEon'

#Limits the volume if its before 8 am
if current_time > eight_am:
    pass
    #print ("Its after 8")
else:
    volume_level = 20
    #print ("Its before 8")

#Monday = 0 | Sunday = 6
if day_of_week_integer== 0:
    webbrowser.open(url0)
    set_volume()
elif day_of_week_integer == 1:
    webbrowser.open(url1)
    set_volume()
elif day_of_week_integer == 2:
    webbrowser.open(url2)
    set_volume()
elif day_of_week_integer == 3:
    webbrowser.open(url3)
    set_volume()
elif day_of_week_integer == 4:
    webbrowser.open(url4)
    set_volume()
elif day_of_week_integer == 5:
    webbrowser.open(url5)
    set_volume()
elif day_of_week_integer == 6:
    webbrowser.open(url6)
    set_volume()

#(url1, new = 2, autoraise=False)

#Remove this code if music autoplays
#Adjust time if network speed is slow  
#time_module.sleep(2)
#keyboard.press_and_release('space')

#Minimizes window (MacOS)
pyautogui.hotkey('command', 'm')

#References
'''
Webbrowser module
https://docs.python.org/3/library/webbrowser.html

Keyboard module
https://pypi.org/project/keyboard/

Datetime module
https://docs.python.org/3/library/datetime.html

strftime() explained
https://www.programiz.com/python-programming/datetime/strftime
'''
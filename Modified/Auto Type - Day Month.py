from calendar import month
from itertools import count
from sqlite3 import Date
import pyautogui
import time

time.sleep(5)

date = 1
maxDate = 30

day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
days = 3

mnth = 12
year = 2022

for i in range (1,maxDate+1):
    pyautogui.typewrite(str(i)+"/"+str(mnth)+"/"+str(year))
    #pyautogui.press("tab")
    #pyautogui.typewrite(day[days-1])
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    if days < 7 :
        days = days + 1
    else :
        days = 1
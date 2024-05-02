from itertools import count
import pyautogui
import time

time.sleep(5)

date = 1
month = "December"
max_date = 31

while date <= max_date :
    pyautogui.typewrite(str(date))
    if date == 1 or date == 21 or date == 31:
        pyautogui.typewrite("st")
    elif date == 2 or date == 22:
        pyautogui.typewrite("nd")
    elif date == 3 or date == 23:
        pyautogui.typewrite("rd")    
    else:   
        pyautogui.typewrite("th")
    pyautogui.typewrite(" "+month)    
    pyautogui.press("enter")
    date= date+1
    
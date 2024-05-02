from calendar import month
from itertools import count
from sqlite3 import Date
import pyautogui
import time

time.sleep(5)

days = 28
mnth = "02"
year = 2023

# rowNo = 155
# i = 2

# while (i < rowNo) :
for i in range (1,days+1):
    pyautogui.typewrite(str(i)+"/"+str(mnth)+"/"+str(year))
    # pyautogui.typewrite(str("0"))
    # pyautogui.typewrite("=sum(e"+str(i)+":e"+str(i+4)+")")

    # i = i+5

    for j in range(0,9):
        pyautogui.press("enter")

from itertools import count
import pyautogui
import time

time.sleep(5)

count = 6

while count <= 27  :
    pyautogui.typewrite(str(count)+".")
    pyautogui.press("enter")   
    pyautogui.typewrite("-")
    pyautogui.press("enter")
    pyautogui.press("enter")
    count = count+1

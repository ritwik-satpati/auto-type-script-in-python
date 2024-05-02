from itertools import count
import pyautogui
import time

time.sleep(5)

count = 1

while count <= 28:
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    count = count+1
    '''time.sleep(2)'''

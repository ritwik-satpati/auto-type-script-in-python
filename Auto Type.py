from itertools import count
import pyautogui
import time

time.sleep(5)

count = 0

while count <= 100 :
    pyautogui.typewrite("This is only for Educational Purposes !")
    # pyautogui.typewrite("Bokachoda "+str(count))
    pyautogui.press("enter")
    count = count+1
    '''time.sleep(2)'''

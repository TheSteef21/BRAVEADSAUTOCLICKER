import pyautogui
from pyautogui import *
import time
from time import sleep
import keyboard
import random
import win32api, win32con

while keyboard.is_pressed ('q') == False:

    time.sleep(0.1)

    pyautogui.FAILSAFE=False
    
    if  pyautogui.locateOnScreen('brave_ad.png', confidence=0.9) != None:
        pyautogui.click(pyautogui.locateCenterOnScreen('brave_ad.png', confidence =0.9))
        print("bravo!")
        time.sleep(0.1)    
    if  pyautogui.locateOnScreen('brave_ad1.png', confidence=0.9) != None:
        pyautogui.click(pyautogui.locateCenterOnScreen('brave_ad1.png', confidence =0.9))
        print("brave!")
        time.sleep(0.1)    
    if  pyautogui.locateOnScreen('brave_ad3.png', confidence=0.9) != None:
        pyautogui.click(pyautogui.locateCenterOnScreen('brave_ad3.png', confidence =0.9))
        print("brave!")
        time.sleep(0.1)




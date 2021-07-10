# BRAVEADSAUTOCLICKER
His function is automatic to click-mode executable.
***
# Welcome to the BRAVEADSAUTOCLICKER wiki! if you need help, he is the best [for it](https://api.whatsapp.com/send/?phone=50769362166&text&app_absent=0) 

## Follow me on [instagram](https://www.instagram.com/steef_gomez) and follow me on ## [youtube](https://www.youtube.com/channel/UCkbyvNwaDv4U8D4nZ_Hc6uQ)

I don't have an instructions page right now but if you know how to install pip packages and another & others stuff, You know, you can do it :D

Just trow it on your notepad.exe (WINDOWS+S), after, save it in wherever place and change the extension .txt for .py

Remember, it is a image recognition bot, you need some packages like [pyautogui](https://pypi.org/project/PyAutoGUI/) and another.

***************************************************************************************************************************************************

`import pyautogui`
`from pyautogui import *`
`import time`
`from time import sleep`
`import keyboard`
`import random`
`import win32api, win32con`

`while keyboard.is_pressed ('q') == False:`

    `time.sleep(0.1)`

    `pyautogui.FAILSAFE=False`
    
    `if  pyautogui.locateOnScreen('brave_ad.png', confidence=0.9) != None:`
        `pyautogui.click(pyautogui.locateCenterOnScreen('brave_ad.png', confidence =0.9))`
        `print("bravo!")`
        `time.sleep(0.1)    `
    `if  pyautogui.locateOnScreen('brave_ad1.png', confidence=0.9) != None:`
        `pyautogui.click(pyautogui.locateCenterOnScreen('brave_ad1.png', confidence =0.9))`
        `print("brave!")`
        `time.sleep(0.1)    `
    `if  pyautogui.locateOnScreen('brave_ad3.png', confidence=0.9) != None:`
        `pyautogui.click(pyautogui.locateCenterOnScreen('brave_ad3.png', confidence =0.9))`
        `print("brave!")`
        `time.sleep(0.1)`

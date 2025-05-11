#!/bin/env python3
# Created by atbswp v0.3.1 (https://git.sr.ht/~rmpr/atbswp)
# on 24 Sep 2023 
import pyautogui
import time
pyautogui.FAILSAFE = False

# click on search
pyautogui.mouseDown(693, 973, 'left')
pyautogui.mouseUp(693, 973, 'left')
time.sleep(0.500)

# click on crypts
pyautogui.mouseDown(681, 547, 'left')
pyautogui.mouseUp(681, 547, 'left')
time.sleep(0.500)

# click on first crypt "GO"
pyautogui.mouseDown(1174, 553, 'left')
pyautogui.mouseUp(1174, 553, 'left')
time.sleep(0.500)

# wait for map to change 1000ms
time.sleep(1.000)

# click crypt (center of screen)
#pyautogui.mouseDown(950, 609, 'left')
#pyautogui.mouseUp(950, 609, 'left')
pyautogui.mouseDown(960, 610, 'left')
pyautogui.mouseUp(960, 610, 'left')


# wait for crypt exploration window to pop-up
time.sleep(0.500)
time.sleep(0.500)


# click on EXPLORE
pyautogui.mouseDown(1135, 864, 'left')
pyautogui.mouseUp(1135, 864, 'left')
time.sleep(0.500)
time.sleep(0.500)
time.sleep(0.500)
time.sleep(0.500)
time.sleep(0.500)
time.sleep(0.500)

# click on first captain's SPEED UP
pyautogui.mouseDown(1234, 199, 'left')
pyautogui.mouseUp(1234, 199, 'left')
time.sleep(0.500)
time.sleep(0.500)

# click on speed up button 5+ times every 200 ms
# 1
pyautogui.mouseDown(1123, 543, 'left')
pyautogui.mouseUp(1123, 543, 'left')
time.sleep(0.200)
# 2
pyautogui.mouseDown(1123, 541, 'left')
pyautogui.mouseUp(1123, 541, 'left')
time.sleep(0.200)
# 3
pyautogui.mouseDown(1123, 541, 'left')
pyautogui.mouseUp(1123, 541, 'left')
time.sleep(0.200)
# 4
pyautogui.mouseDown(1123, 541, 'left')
pyautogui.mouseUp(1123, 541, 'left')
time.sleep(0.200)
# 5
pyautogui.mouseDown(1123, 541, 'left')
pyautogui.mouseUp(1123, 541, 'left')
time.sleep(0.200)
pyautogui.mouseDown(1123, 541, 'left')
pyautogui.mouseUp(1123, 541, 'left')
time.sleep(0.200)
pyautogui.mouseDown(1123, 541, 'left')
pyautogui.mouseUp(1123, 541, 'left')

# wait for carter to go there and come back (<20s one way)
time.sleep(40.00)


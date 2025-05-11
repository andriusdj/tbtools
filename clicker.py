#!/bin/env python3
import pyautogui
import time
import sys

pyautogui.FAILSAFE = False

loop = int(sys.argv[1]) if len(sys.argv) > 1 else 0

size = pyautogui.size()
print(f"Screen size: {size}")

pos = pyautogui.position()
print(f"Fixed mouse position: {pos}")

if loop:
    print(f"Clicks: {loop}")
else:
    print("Clicks: unlimited")

def has_moved(pos):
    current_pos = pyautogui.position()
    if current_pos.x == pos.x and current_pos.y == pos.y:
        return False
    return True

while True:
    pos = pyautogui.position()
    loop = loop - 1
    print(f"Click#: {abs(loop)}")
    pyautogui.mouseDown(pos.x, pos.y, 'left')
    pyautogui.mouseUp(pos.x, pos.y, 'left')
    #time.sleep(0.020)
    if has_moved(pos):
        print(f"Mouse moved. Exiting.")
        break
    if loop == 0:
        print(f"Repetitions reached. Exiting.")
        break



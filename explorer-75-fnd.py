#!/bin/env python3
import pyautogui
import time
import cv2
import numpy as np
import pyautogui
import random
import time
import platform
import subprocess
import os
import mss
import sys


import tesserocr
from PIL import Image
from PIL import ImageEnhance 
from PIL import ImageOps
from PIL import ImageFilter

pyautogui.FAILSAFE = False

width, height = pyautogui.size()

def log(text):
    print(text, end='', flush=True)

def click(x, y):
    pyautogui.mouseDown(x, y, 'left')
    pyautogui.mouseUp(x, y, 'left')
    log('.')

def click_on_search():
    if height == 1200:
        click(692, 1099)
    else:
        click(692, 973)

def click_on_crypts():
    if height == 1200:
        click(682, 615)
    else:
        click(682, 547)
        
def go_to_first_crypt():
    if height == 1200:
        click(1213, 648)
    else:
        click(1174, 592)

def explore():
    if height == 1200:
        click(1139, 930)
    else:
        click(1135, 864)

def open_speed_up():
    if height == 1200:
        click(1236, 212)
    else:
        click(1234, 199)

def use_speedups(repeat, wait):
    while repeat > 0:
        if height == 1200:
            click(1124, 612)
        else:
            click(1123, 543)
        repeat = repeat - 1
        time.sleep(wait)

def region_grabber(region):
    x1 = region[0]
    y1 = region[1]
    w = region[2]
    h = region[3]

    region = x1, y1, w, h
    with mss.mss() as screenshot:
        return screenshot.grab(region)

def get_crypt_type(loc=0, loop=0):
    time.sleep(0.100)

    common_epic_region_1200p = (900, 375, 1050, 395)
    rare_locked_region_1200p = (900, 333, 1050, 356)

    common_epic_region_1080p = (877, 409, 1043, 431)
    rare_locked_region_1080p = (877, 409, 1043, 431)

    check_regions = [
        common_epic_region_1200p if height == 1200 else common_epic_region_1080p,
        rare_locked_region_1200p if height == 1200 else rare_locked_region_1080p,
    ]

    region_index = 0
    for check_region in check_regions:
        
        # im = region_grabber(region=(800, 369, 1100, 400))
        im = region_grabber(region=check_region)    
        
        img = Image.frombytes("RGB", im.size, im.bgra, "raw", "BGRX")
        
        w, h = img.size
        img = img.resize((w*2, h*2))  
        img = img.convert('L')
        img = img.point(lambda x: 0 if x < 150 else 255, '1')
        img = ImageOps.invert(img)
    
        with tesserocr.PyTessBaseAPI() as api:
            api.SetImage(img)
            
            text = api.GetUTF8Text().strip()
            text = text.strip("-.,_-~/|\\()[]")

            #img.save(f"./2025-test_loop{loop}-loc{loc}-region{region_index}-text[{text}].png") # debug

            if text == 'Crypt':
                return 'common'
            
            if text == 'Rare Crypt':
                return 'rare'
            
            if text == 'Epic Crypt':
                return 'epic'

        region_index = region_index + 1

    return False

def open_rare():
    if height == 1200:
        click(960, 925)
    else:
        click()

if len(sys.argv) > 1 and sys.argv[1] == 'test':
    print(f"Size: {width}x{height}")
    try:
        while True:
            x, y = pyautogui.position()
            pos = f"X: {str(x).rjust(4)} Y: {str(y).rjust(4)}"
            sys.stdout.flush()
    except KeyboardInterrupt:
        print(pos)
        sys.exit()

loop = int(sys.argv[1]) if len(sys.argv) > 1 else 1

def crypt_open(loc, loop):
    
    locations_1080p = [ [953,607], [1068, 552], [1184, 614], [1065, 666], [959, 724], [842, 667], [732, 613], [848, 555], [957, 494] ]
    locations_1200p = [ [958,678], [1063, 621], [1178, 674], [1065, 733], [953, 788], [838, 729], [726, 670], [842, 614], [953, 559] ]
    locations = locations_1200p if height == 1200 else locations_1080p
    try:
        click(locations[loc][0], locations[loc][1])
    except IndexError:
        raise IndexError(f"Crypt could not be opened at location: {loc}")
    # wait for window to open
    time.sleep(0.800)
    crypt = get_crypt_type(loc=loc, loop=loop)
    time.sleep(0.100)
    if not crypt:
        log(".")
        pyautogui.press("esc")
        return False
    
    log(f'Found {crypt}.')
    return True

def open_crypt_dialog(loop=0):
    t = 0
    log("Looking for crypt: ")
    while not crypt_open(loc=t, loop=loop):
        t = t + 1
                
    # wait for crypt exploration window to pop-up
    time.sleep(1.0)

count = 1
while True:

    log(f"{count}) ")
    click_on_search()
    time.sleep(0.500)

    # click on crypts
    click_on_crypts()
    time.sleep(0.500)

    # click on first crypt "GO"
    go_to_first_crypt()
    time.sleep(0.500)

    # wait for map to change 1000ms
    time.sleep(1.000)
    try:
        open_crypt_dialog(loop=loop)
    except IndexError as e:
        log(str(e))
        time.sleep(2.00)
        print('Restart.')
        continue

    if get_crypt_type() == 'rare':
        open_rare()
        time.sleep(0.400)

    # click on EXPLORE
    explore()
    time.sleep(5.0)

    # click on first captain's SPEED UP
    open_speed_up()
    time.sleep(1.0)

    use_speedups(repeat=5, wait=0.200)

    # wait for carter to go there and come back (<20s one way)
    time.sleep(40.00)
    
    loop = loop - 1
    count = count + 1

    if loop <= 0:
        break

    print('Done.')


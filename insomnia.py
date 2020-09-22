#!/usr/bin/python3

import time 
import pyautogui

if __name__ == "__main__":
    count = 0
    xoffset = 1
    yoffset = 1
    sleeptime = 60

    max_x, max_y = pyautogui.size()
    max_x -= 1
    max_y -= 1
    print('Display size: x=' + str(max_x) + ', y=' + str(max_y))

    while True:
        pyautogui.moveRel(xoffset, yoffset)
        x, y = pyautogui.position()
        if x == max_x or x == 0:
            xoffset *= -1
        if y == max_y or y == 0:
            yoffset *= -1
        print('Insomnia: ' + time.ctime())
        time.sleep(sleeptime)
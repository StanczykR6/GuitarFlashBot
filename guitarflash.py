import cv2
import numpy as np
from matplotlib import pyplot as plt
import mss
from PIL import Image
import threading
from pynput.keyboard import Key, Controller
import time

pressed = []
keyboard = Controller()

def guitarBot():
    greenPressed = False
    redPressed = False
    yellowPressed = False
    bluePressed = False
    orangePressed = False
    #noteLoop()

    with mss.mss() as sct:
        monitor = {"top": 575, "left": 520, "width": 375, "height": 30}
        meter = {"top": 490, "left": 915, "width": 20, "height": 20}

    while(1):
        img = np.array(sct.grab(monitor))
#        starpower = np.array(sct.grab(meter))

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lowerGreen = np.array([45, 75, 100])
        upperGreen = np.array([70, 255, 255])
        greenMask = cv2.inRange(hsv, lowerGreen, upperGreen)
        greenMask[0:60,125:750] = 0

        lowerRed = np.array([0, 100, 100])
        upperRed = np.array([5, 255, 255])
        redMask = cv2.inRange(hsv, lowerRed, upperRed)
        redMask[0:60,0:200] = 0
        redMask[0:60,250:750] = 0

        lowerYellow = np.array([26, 75, 100])
        upperYellow = np.array([40, 255, 255])
        yellowMask = cv2.inRange(hsv, lowerYellow, upperYellow)
        yellowMask[0:60,0:425] = 0
        yellowMask[0:60,450:750] = 0

        lowerBlue = np.array([100, 100, 100])
        upperBlue = np.array([130, 255, 255])
        blueMask = cv2.inRange(hsv, lowerBlue, upperBlue)
        blueMask[0:60,0:550] = 0
        blueMask[0:60,600:750] = 0

        lowerOrange = np.array([10, 100, 100])
        upperOrange = np.array([12, 255, 255])
        orangeMask = cv2.inRange(hsv, lowerOrange, upperOrange)
        orangeMask[0:60,0:700] = 0

        mask = greenMask + redMask + yellowMask + blueMask + orangeMask
        res = cv2.bitwise_and(img, img, mask = mask)

        for g in greenMask:
            if g.any() != 0 and not greenPressed:
                #pressed.append('a')
                keyboard.press('a')
                greenPressed = True
                break
        else:
            keyboard.release('a')
            greenPressed = False

        for r in redMask:
            if r.any() != 0 and not redPressed:
                #pressed.append('a')
                keyboard.press('s')
                redPressed = True
                break
        else:
            keyboard.release('s')
            redPressed = False

        for y in yellowMask:
            if y.any() != 0 and not yellowPressed:
                #pressed.append('a')
                keyboard.press('d')
                yellowPressed = True
                break
        else:
            keyboard.release('d')
            yellowPressed = False

        for b in blueMask:
            if b.any() != 0 and not bluePressed:
                #pressed.append('a')
                keyboard.press('j')
                bluePressed = True
                break
        else:
            keyboard.release('j')
            bluePressed = False

        for o in orangeMask:
            if o.any() != 0 and not orangePressed:
                #pressed.append('a')
                keyboard.press('k')
                orangePressed = True
                break
        else:
            keyboard.release('k')
            orangePressed = False

        cv2.imshow('masked', res)
        cv2.imshow('screen', img)
        #cv2.imshow('star power', starpower)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

def noteLoop():
    threading.Timer(0.05, noteLoop).start()
    if 'a' in pressed:
        keyboard.press('a')

    if 's' in pressed:
        keyboard.press('s')

    if 'd' in pressed:
        keyboard.press('d')

    if 'j' in pressed:
        keyboard.press('j')

    if 'k' in pressed:
        keyboard.press('k')


if __name__ == '__main__':
    guitarBot()
    #guitarTest()

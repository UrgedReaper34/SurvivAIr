from re import A
import selenium
import numpy as np
import pyautogui
from selenium import webdriver
import time

import win32api, win32con
import cv2
import numpy as np
import win32gui, win32ui, win32con, win32api
import keyboard




def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

window_x = 0.0
window_y = 100 # The tool bar in chrome is 100 pixels (or so) tall

# Too high resolution and the dataset gets too big.  This is the size of the window to create
width = 800
height = 600

# size of the game window (the playable area)
window_width = width 
window_height = height - window_y

def open_and_size_browser_window(width, height, x_pos = 0, y_pos = 0, url = 'https://www.surviv.io'):

#     opens the browser window   
    driver = webdriver.Edge("C:\\Users\\johnt\\Documents\\VScodePY\\work\\demo\\surviv.io AI\\msedgedriver.exe")

#     maximises the window
    
    
    
    
    
#     goes to slither.io
    driver.get(url)
    a = False
    print("Finding start button....")
    while a == False:
        if pyautogui.locateOnScreen('surviv.io AI\\surviv.io buttons\\maximize.png', confidence = 0.7, grayscale = True) != None:
            info = pyautogui.locateOnScreen('surviv.io AI\\surviv.io buttons\\maximize.png', confidence = 0.7, grayscale = True)
            print(info)
            print("I can see it")
            time.sleep(0.5)
            a = True

        if pyautogui.locateOnScreen('surviv.io AI\\surviv.io buttons\\maximize.png', confidence = 0.7, grayscale = True) == None:
            print("I am unable to see it")
            time.sleep(0.5)
            a = False

    left = str(info[0]).strip("left=")
    top = str(info[1]).strip("top=")
    click(int(left) + 5, int(top) + 5)

    return driver

def join_game():
    a = False
    while a == False:
        if pyautogui.locateOnScreen("surviv.io AI\\surviv.io buttons\\no2.png", confidence = 0.8) != None:
            info = pyautogui.locateOnScreen("surviv.io AI\\surviv.io buttons\\no2.png", confidence = 0.8)
            print(info)
            print("I can see it!")
            a = True
            time.sleep(0.5)

        if pyautogui.locateOnScreen("surviv.io AI\\surviv.io buttons\\no2.png", confidence = 0.8) == None:
            print("I am unable to see it!")
            time.sleep(0.5)
    left = str(info[0]).strip("left=")
    top = str(info[1]).strip("top=")
    click(int(left) + 10, int(top) + 10)
    print("Finding the battle button....")
    seebattlebutton = False
    while seebattlebutton == False:
        if pyautogui.locateOnScreen("surviv.io AI\\surviv.io buttons\\battle2.png", confidence = 0.8, grayscale = True) != None:
            info = pyautogui.locateOnScreen("surviv.io AI\\surviv.io buttons\\battle2.png", confidence = 0.8, grayscale = True)
            print(info)
            print("I can see it!")
            seebattlebutton = True
            time.sleep(0.5)

        if pyautogui.locateOnScreen("surviv.io AI\\surviv.io buttons\\battle2.png", confidence = 0.8, grayscale = True) == None:
            print("I am unable to see it!")
            time.sleep(0.5)
    left = str(info[0]).strip("left=")
    top = str(info[1]).strip("top=")
    click(int(left) + 250, int(top) + 10)
    time.sleep(1)
    click(int(left) + 250, int(top) + 10)
    time.sleep(1)
    click(int(left) + 250, int(top) + 10)
    time.sleep(1)
    seenextbutton = False
    while seenextbutton == False:
        if pyautogui.locateOnScreen("surviv.io AI\\surviv.io buttons\\next.png", confidence = 0.8, grayscale = True) != None:
            info = pyautogui.locateOnScreen("surviv.io AI\\surviv.io buttons\\next.png", confidence = 0.8, grayscale = True)
            print(info)
            print("I can see it!")
            seenextbutton = True
            time.sleep(0.5)
            left = str(info[0]).strip("left=")
            top = str(info[1]).strip("top=")
            click(int(left) + 2, int(top) + 10)
            click(int(left) + 5, int(top) + 20)
            time.sleep(0.5)
            click(int(left) + 2, int(top) + 10)
            click(int(left) + 5, int(top) + 20)
            time.sleep(0.5)
            click(int(left) + 2, int(top) + 10)
            click(int(left) + 5, int(top) + 20)
            time.sleep(0.5)
            click(int(left) + 2, int(top) + 10)
            click(int(left) + 5, int(top) + 20)
            time.sleep(0.5)

        if pyautogui.locateOnScreen("surviv.io AI\\surviv.io buttons\\next.png", confidence = 0.8, grayscale = True) == None:
            print("I am unable to see it!")
            time.sleep(0.5)
    print("Joined the game!!!")


def moving_to_centre():  
    dead = False
    while True:
        info = pyautogui.locateOnScreen('surviv.io AI\\surviv.io buttons\\minimap.png', confidence = 0.5, grayscale = True)
        left = str(info[0]).strip("left=")
        top = str(info[1]).strip("top=")
        pic = pyautogui.screenshot(region = (info)) # takes the screenshot of the minimap
        width, height = pic.size
    #Finds the yellow thingy, which basically represents the player on the minimap
        yellow_found = False
        while yellow_found == False:
            for x2 in range(0, width, 3): # skips 2 out of 2 pixels
                for y2 in range(0, height, 3):
                    r, g, b = pic.getpixel((x2, y2))
                    if r == 255 and g == 255 and b == 0:
                        yellow_found == True
                        print("Player has been found!")
                    else:
                        print("Player not found for now!")
                        pass
        match_found = False
        while match_found == False: # finds the light green thing at the edge of the minimap, which is black in color
            for x in range(0, width, 3): # skips 2 out of 2 pixels
                for y in range(0, height, 3):
                    r, g, b = pic.getpixel((x, y))
                    a = g - r
                    if a == 128 and r == b:# checks if the pixel is even light green
                        r2, g2, b2 = pic.getpixel((x + 2, y)) # checks whether the pixel on the right is black
                        if r2 == 0 and g2 == 0 and b2 == 0:
                            print("A Match was found")
                            match_found = True
                        else:
                            print("Match was not found!")
                            pass
                        r2, g2, b2 = pic.getpixel((x - 2, y)) # checks whether the pixel on the left is black
                        if r2 == 0 and g2 == 0 and b2 == 0:
                            print("A Match was found")
                            match_found = True
                        else:
                            print("Match was not found!")
                            pass
                        r2, g2, b2 = pic.getpixel((x, y + 2)) # checks whether the pixel above is black
                        if r2 == 0 and g2 == 0 and b2 == 0:
                            print("A Match was found")
                            match_found = True
                        else:
                            print("Match was not found!")
                            pass
                        r2, g2, b2 = pic.getpixel((x, y - 2)) # checks whether the pixel below is black
                        if r2 == 0 and g2 == 0 and b2 == 0:
                            print("A Match was found")
                            match_found = True
                        else:
                            print("Match was not found!")
                            pass  

        
    

    # Determining which directon the player needs to move based on the direction of the line
        print("Player is located at: {}".format((x2, y2)))
        print("Centre is located at: {}".format((x, y)))
        print("X move: {}, Y move: {}".format((x - x2), (y - y2)))

                    
        
                    
        
    



driver = open_and_size_browser_window(width = width, height = height)
join_game()
moving_to_centre()

shouldClick = True
keyRelease = True

'''if keyboard.is_pressed('q') and keyRelease:
        keyRelease = False
        shouldClick = not shouldClick
    if not keyboard.is_pressed('q'):
        keyRelease = True
    if shouldClick:
        moving_to_centre()
        print("HII")'''
    
    
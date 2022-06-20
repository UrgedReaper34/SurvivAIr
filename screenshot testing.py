import pyautogui
import numpy as np
import cv2 as cv
def browser_coordinates_cal(top_left, bottom_right):
    first_input = top_left[0]
    second_input = top_left[1]
    third_input = bottom_right[0] - top_left[0]
    fourth_input = bottom_right[1] - top_left[1]

    return first_input, second_input, third_input, fourth_input

    
first_input, second_input, third_input, fourth_input = browser_coordinates_cal([145, 120], [1920, 1080]) #input coordinates like this([x, y], [x, y])

while(True):
    screenshot = pyautogui.screenshot(region = (first_input, second_input, third_input, fourth_input))
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)


    if cv.waitKey(1) == ord('q'):
        break
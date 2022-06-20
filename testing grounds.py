import cv2 as cv
import numpy as np
import os
import pyautogui
from PIL import Image
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def browser_coordinates_cal(top_left, bottom_right):
    first_input = top_left[0]
    second_input = top_left[1]
    third_input = bottom_right[0] - top_left[0]
    fourth_input = bottom_right[1] - top_left[1]

    return first_input, second_input, third_input, fourth_input


#gets all the file paths from the folder
def getAllFiles(path):
    list_of_files = []
    for root, dirs, files in os.walk(path):
	    for file in files:
		    list_of_files.append(os.path.join(root,file))
    return list_of_files
            
list_of_files = getAllFiles("survivlootimages2")



# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub

def findClickPositions(surviv_img, first_input, second_input, third_input, fourth_input, threshold=0.7, debug_mode=None):
        
    # https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html
    surviv_img = cv.imread(surviv_img, cv.IMREAD_UNCHANGED)
    screenshot = Image.grab()
    screenshot = np.array(screenshot)
    screenshot = screenshot[:, :, ::-1].copy()

    
    # Save the dimensions of the needle image
    surviv_img_w = surviv_img.shape[1]
    surviv_img_h = surviv_img.shape[0]

    # There are 6 methods to choose from:
    # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(screenshot, surviv_img, method)

    # Get the all the positions from the match result that exceed our threshold
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    #print(locations)

    # You'll notice a lot of overlapping rectangles get drawn. We can eliminate those redundant
    # locations by using groupRectangles().
    # First we need to create the list of [x, y, w, h] rectangles
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), surviv_img_w, surviv_img_h]
        # Add every box to the list twice in order to retain single (non-overlapping) boxes
        rectangles.append(rect)
        rectangles.append(rect)
    # Apply group rectangles.
    # The groupThreshold parameter should usually be 1. If you put it at 0 then no grouping is
    # done. If you put it at 2 then an object needs at least 3 overlapping rectangles to appear
    # in the result. I've set eps to 0.5, which is:
    # "Relative difference between sides of the rectangles to merge them into a group."
    rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
    #print(rectangles)

    points = []
    if len(rectangles):
        #print('Found needle.')

        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        # Loop over all the rectangles
        for (x, y, w, h) in rectangles:

            # Determine the center position
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            # Save the points
            points.append((center_x, center_y))

    return points

first_input, second_input, third_input, fourth_input = browser_coordinates_cal([145, 120], [1920, 1080]) #input coordinates like this([x, y], [x, y])


for file in list_of_files:
    points = findClickPositions(str(file), first_input, second_input, third_input, fourth_input)
    if len(points) >= 1:
        print("The image: " + file + " has been located at" + str(points))
        
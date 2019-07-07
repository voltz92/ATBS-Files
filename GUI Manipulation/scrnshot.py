# pyautogui screenshotting
import pyautogui

# to capture the screen use 

pyautogui.screenshot('wow.png') # gets saved in current working directory

# without any argument it creates an image object 

# to search for the occurence of an image on the screen 
# use pyautogui.locateOnScreen('image') <<< returns a tuple containing location coords of the image on screen and pair of values describing the height and width of the image

# use pyautogui.locateCenterOnScreen('image') << returns the coords of the center of the image on the screen

## screen must have exact match of the image to get data otherwise None returned

# use the Documentation to learn more



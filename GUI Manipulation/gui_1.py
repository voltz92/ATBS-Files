# gui manipulation using pyautogui module

import pyautogui

# get screensize 

print(pyautogui.size())  # returns a tuple of width and height

# move mouse cursor to a specific coordinate  >>  starts at (0,0) at top left and (width-1,height-1) at bottom right
# x-coords incrase to the left. y-coords incrs down

#pyautogui.moveTo(20,20, duration = 1)  # <<< moves the cursor to argument location. duration modifier can be used to slow it down

# can use relative movement

#pyautogui.moveRel(20,-20,duration = 2) # -20 in y moves upwards. mouse will move relative to current location

# can use pyautogui.position() to get the location of the current pointer position

# use click(x,y) << to click at a specific location

pyautogui.click(501,18) # without args it just clicks at current location
 
# doubleclick/rightclick/middleclick() all available

#pyautogui.drag/dragto/dragrel() methods allow for dragging the mouse( ie click and hold)

# using the console and pyautogui.displayMousePosition() method << we can continually show the current cursor location


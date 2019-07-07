# pyautogui keyboard control 

import pyautogui
# to change focus to the notepad window i have setup to the left
pyautogui.click(100,100); pyautogui.typewrite('Hello World!!!', interval= 0.1);# to type in a string, the interval modifier introduces a delay between each character output 

# pyautogui.KEYBOARD_KEYS << displays list of available 'key names' in the pyautogui module

#pyautogui.press('f1') << will press the f1 key once

# to use hotkeys/shortcut key combinations 

#pyautogui.hotkey('ctrl','o')
import pyautogui
import time

next_x = 1878
next_y = 960

screen_start_y = 290
screen_end_y = 810 

screen_start_x = 977
screen_end_x = 1904

start_time = time.time()  # start time
pyautogui.moveTo(next_x, next_y) # you can set the position of the mouse (x, y)

import pyautogui
import time

def watchTime(start_time):
    now_time = time.time() # current time
    elapsed_time = now_time - start_time # elapsed time
    if elapsed_time >= 60: # 60 seconds
        y = screen_start_y
        while y <= screen_end_y:
            x = screen_start_x
            while x <= screen_end_x:
                pyautogui.moveTo(x, y)
                pyautogui.click()
                x += 50
            y += 40
        start_time = time.time()
    return start_time

while (True):
	pyautogui.click() # click the mouse
	time.sleep(5)
	pyautogui.moveTo(next_x, next_y) # you can set the position of the mouse (x, y)
	start_time = watchTime(start_time)

print("Done")

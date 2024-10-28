import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position() # we get the position of the mouse
        
        print(f"mouse position: X: {x}, Y: {y}")
        
        # one minute
        time.sleep(1)
except KeyboardInterrupt:
    print("\Stop program.")


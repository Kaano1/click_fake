import pyautogui
import time

pyautogui.moveTo(196, 33) # you can set the position of the mouse (x, y)
while (True):
	time.sleep(29)
	if (pyautogui.position() != (196, 33)):
		break
	time.sleep(1)
	pyautogui.click() # click the mouse


print("Done")

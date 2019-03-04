# import the necessary packages
import numpy as np
import pyautogui
import imutils
import cv2
	
# take a screenshot of the screen and store it in memory, then
# convert the PIL/Pillow image to an OpenCV compatible NumPy array
# and finally write the image to disk
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("in_memory_to_disk.png", image)


# this time take a screenshot directly to disk
#pyautogui.screenshot("straight_to_disk.png")

# we can then load our screenshot from disk in OpenCV format
#image = cv2.imread("straight_to_disk.png")
#cv2.imshow("Screenshot", imutils.resize(image, width=600))
#cv2.waitKey(0)
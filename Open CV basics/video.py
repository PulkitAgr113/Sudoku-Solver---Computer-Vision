import cv2
import sys
import numpy as np

#Reading the video
cap = cv2.VideoCapture(sys.argv[1])
cap2 = cv2.VideoCapture(0)

#Default mode and dimensions
mode = 'BGR'
width = 1280
height = 720
counter = 0

if len(sys.argv) >= 4:
	width = int(sys.argv[2])
	height = int(sys.argv[3])

while True:
	ret, frame = cap.read()
	ret2, frame2 = cap2.read()
	frame = cv2.resize(frame,(width,height))
	frame2 = cv2.resize(frame2,(width//4,height//4))
	counter += 1

	#Check if video has ended, and loop
	if counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
		counter = 0
		cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

	#Blue cross at center of screen
	frame = cv2.line(frame,(width//2-100,height//2+100),(width//2+100,height//2-100),(255,0,0),10)
	frame = cv2.line(frame,(width//2+100,height//2+100),(width//2-100,height//2-100),(255,0,0),10)

	#Red border of the WebCam feed
	bordersize = 10
	frame2 = cv2.copyMakeBorder(
	    frame2,
	    top = bordersize,
	    bottom = bordersize,
	    left = bordersize,
	    right = bordersize,
	    borderType = cv2.BORDER_CONSTANT,
	    value = (0,0,255)
	)

	#Changing mode of WebCam feed based on key pressed
	key = cv2.waitKey(1)

	if key == 49:
		mode = 'BGR'
	elif key == 50:
		mode = 'GRAY'
	elif key == 51:
		mode = 'BLUR'
	elif key == ord('q'):
		break

	if mode == 'GRAY':
		frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
	elif mode == 'BLUR':
		frame2 = cv2.GaussianBlur(frame2,(19,19),0)

	#Putting WebCam feed in a small rectangle on the upper left corner of given video
	if mode == 'GRAY':
		newFrame = cv2.merge((frame2,frame2,frame2))
		frame[0:height//4+2*bordersize,0:width//4+2*bordersize,:] = newFrame
	else:
		frame[0:height//4+2*bordersize,0:width//4+2*bordersize,:] = frame2

	cv2.imshow(sys.argv[1],frame)

cap.release()
cap2.release()
cv2.destroyAllWindows()
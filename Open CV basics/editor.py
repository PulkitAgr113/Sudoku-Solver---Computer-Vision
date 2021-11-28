import cv2
import sys
import numpy as np

#Reading the image and resizing
if len(sys.argv) == 1:
	image = np.zeros((1280,720,3))
	image = image + 255

elif len(sys.argv) == 2:
	image = cv2.imread(sys.argv[1])
	if image is None:
		image = np.zeros((1280,720,3))
		image = image + 255
	image = cv2.resize(image,(1280,720))

else:
	image = cv2.imread(sys.argv[1])
	if image is None:
		image = np.zeros((1280,720,3))
		image = image + 255
	image = cv2.resize(image,(int(sys.argv[2]),int(sys.argv[3])))

#Default color
color = 'Red'
print('Red')
cv2.imshow('Editor',image)

#Draw point of chosen color at mouse-click
def draw_point(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDBLCLK or event == cv2.EVENT_RBUTTONDBLCLK:
		if color == 'Red':
			cv2.circle(image,(x,y),2,(0,0,255),5)
		elif color == 'Green':
			cv2.circle(image,(x,y),2,(0,255,0),5)
		elif color == 'Blue':
			cv2.circle(image,(x,y),2,(255,0,0),5)

while True:
	cv2.setMouseCallback('Editor',draw_point)
	
	#Changing color of point based on key pressed
	key = cv2.waitKey(1)

	if key == ord('r'):
		if color != 'Red':
			print('Red')
		color = 'Red'

	elif key == ord('g'):
		if color != 'Green':
			print('Green')
		color = 'Green'

	elif key == ord('b'):
		if color != 'Blue':
			print('Blue')
		color = 'Blue'

	elif key == ord('q'):
		if len(sys.argv) > 1:
			cv2.imwrite(sys.argv[1],image)
		else:
			cv2.imwrite('image.jpg',image)
		break

	cv2.imshow('Editor',image)

cv2.destroyAllWindows()
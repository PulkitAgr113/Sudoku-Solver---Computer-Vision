import cv2
import numpy as np

# Reading and showing
image = cv2.imread("lena.png")
resize = cv2.resize(image,(256,256))
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(19,19),0)
cv2.imshow("Picture",image)
cv2.imshow("Resized",resize)
cv2.imshow("Gray",gray)
cv2.imshow("Blur",blur)

#Drawing lines/rectangles/circles
img = np.zeros((512,512,3))
img = cv2.line(img,(0,0),(511,511),(255,0,0),10)
img = cv2.rectangle(img,(100,100),(400,400),(0,0,255),10)	
img = cv2.circle(img,(250,250),50,(0,255,255),10)
cv2.putText(img,'Computer Vision',(120,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3,cv2.LINE_AA)

#Drawing polygons
pts = np.array([[25,70], [25,160], [110,200], [200,160], [200,70], [110,20]], np.int32)
pts = pts.reshape(-1,1,2)
cv2.polylines(img,[pts],True,(255,255,255))
cv2.imshow("Drawing",img)

#Accessing webcam
cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	cv2.imshow("capture",frame)

	key = cv2.waitKey(1)

	if key == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
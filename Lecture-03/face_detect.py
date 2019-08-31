import cv2

camera = cv2.VideoCapture(1)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')


while True:
	ret,img = camera.read()
	
	if ret==False:
		continue
	faces= face_detector.detectMultiScale(img,1.1,5)
	for face in faces:
		x,y,w,h = face
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

	cv2.imshow("Title",img)
	key = cv2.waitKey(1) & 0xFF
	if key==ord('q'):
		break

camera.release()
cv2.destroyAllWindows()





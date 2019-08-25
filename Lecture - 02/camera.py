import cv2


cam  = cv2.VideoCapture(0)

while True:
	ret, frame = cam.read()
	if ret:
		cv2.imshow("Camera", frame)
		cv2.imshow("BGR", frame[...,[2,1,0]])
		if cv2.waitKey(1) & 0xFF == ord("q"):
			break
	else:
		break

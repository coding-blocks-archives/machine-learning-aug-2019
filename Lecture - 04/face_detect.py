import cv2
import numpy as np

camera = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

BASE_DIR = "./data/"
name = input("Enter your name : ")
faces_data = []


cnt = 0
while True:
	ret,img = camera.read()
	
	if ret==False:
		continue
	faces= face_detector.detectMultiScale(img,1.3,5)
	
	if(len(faces)==0):
		print("0 face detected")
		continue

	x,y,w,h = faces[0]
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
	cropped_face = img[y:y+h,x:x+w]
	cropped_face = cv2.resize(cropped_face,(100,100))

	cv2.imshow("Title",img)
	cv2.imshow("Cropped Face",cropped_face)
	key = cv2.waitKey(1) & 0xFF
	if key==ord('q'):
		break

	cnt += 1
	if cnt%10==0:
		faces_data.append(cropped_face)
		print("Saving pic ",(cnt/10))
	


camera.release()
cv2.destroyAllWindows()

faces_data = np.asarray(faces_data)
np.save(BASE_DIR+name+".npy",faces_data)




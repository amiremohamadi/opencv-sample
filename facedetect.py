import cv2

img_path = 'friends.png'
casc_path = 'cascade.xml'

face_cascade = cv2.CascadeClassifier(casc_path)

img = cv2.imread(img_path)

faces = face_cascade.detectMultiScale(img)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 4)


cv2.imshow('window', img)
cv2.waitKey(0)
